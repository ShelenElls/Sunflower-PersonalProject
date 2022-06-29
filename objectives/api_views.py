from asyncio import tasks
from pyexpat import model
from webbrowser import get
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
import json

from common.json import ModelEncoder

from .models import Status, Objective


class StatusEncoder(ModelEncoder):
    model = Status
    properties = [
        "name"
    ]

class ObjectiveEncoder(ModelEncoder):
    model = Objective
    properties = [
        "id",
        "description",
        "due_date",
        "status",
        "monthly_income", 
    ]
    encoders = {
        "status": StatusEncoder(),

    }



@require_http_methods(["GET", "POST"])
def api_objectives(request):
    if request.method == "GET":
        status = Status.objects.get(name="PENDING")
        tasks = Objective.objects.filter(status=status)
        return JsonResponse(
            {"tasks": tasks},
            encoder=ObjectiveEncoder,
            safe=False,
        )
    else:
        content = json.loads(request.body)
        newtask = Objective.create(**content)
        return JsonResponse(
            newtask,
            encoder=ObjectiveEncoder,
            safe=False,
        )


@require_http_methods(["GET", "DELETE", "PUT"])
def api_objective(request, pk):
    if request.method == "GET":
        task = Objective.objects.get(id=pk)
        return JsonResponse(
            task,
            encoder=ObjectiveEncoder,
            safe=False,
        )
    elif request.method == "PUT":
        content = json.loads(request.body)
        Objective.objects.filter(id=pk).update(**content)
        service = Objective.objects.get(id=pk)
        return JsonResponse(
        service,
        encoder=ObjectiveEncoder,
        safe=False,
        )
    else:
        count, _ = Objective.objects.filter(id=pk).delete()
        return JsonResponse({"deleted": count > 0})



@require_http_methods(["PUT"])
def api_finished_obj(request, pk):
    obj = Objective.objects.get(id=pk)
    obj.completed()
    return JsonResponse(
        obj, 
        encoder=ObjectiveEncoder,
        safe=False,
    )

@require_http_methods(["PUT"])
def api_cancelled_obj(requests, pk):
    cancel = Objective.objects.get(id=pk)
    cancel.cancelled()
    return JsonResponse(
        cancel,
        encoder=ObjectiveEncoder,
        safe=False,
    )

@require_http_methods(["GET"])
def api_show_all(requests):
    history = Objective.objects.all()
    return JsonResponse(
        history,
        encoder=ObjectiveEncoder,
        safe=False
    )







# original work with just templates and html/ prior to react and JSON 


# from django.shortcuts import render
# from django.shortcuts import redirect
# from django.views.generic.list import ListView
# from django.views.generic.edit import CreateView, UpdateView
# from django.contrib.auth.mixins import LoginRequiredMixin

# from objectives.models import Objective

# # Create your views here.

# class ObjectivesCreateView(LoginRequiredMixin, CreateView):
#     model = Objective
#     template_name = "objectives/create.html"
#     fields = ["name", "description", "due_date"]

#     def form_valid(self, form):
#         item = form.save(commit=False)
#         item.owner = self.request.user
#         item.save()
#         return redirect("list_objectives")

# class ObjectivesListView(LoginRequiredMixin, ListView):
#     model = Objective
#     template_name = "objectives/list.html"

#     # def form_valid(self, form):
#     #     item = form.save(commit=False)
#     #     item.owner = self.request.user
#     #     item.save()
#     #     return redirect("list_objectives")

# class ObjectivesUpdateView(LoginRequiredMixin, UpdateView):
#     model = Objective
#     template_name = "objectives/edit.html"
#     fields = ["name", "description", "due_date"]