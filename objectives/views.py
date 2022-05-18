from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from objectives.models import Objective

# Create your views here.

class ObjectivesCreateView(LoginRequiredMixin, CreateView):
    model = Objective
    template_name = "objectives/create.html"
    fields = ["name", "description", "due_date"]

    def form_valid(self, form):
        item = form.save(commit=False)
        item.owner = self.request.user
        item.save()
        return redirect("list_objectives")

class ObjectivesListView(LoginRequiredMixin, ListView):
    model = Objective
    template_name = "objectives/list.html"

    # def form_valid(self, form):
    #     item = form.save(commit=False)
    #     item.owner = self.request.user
    #     item.save()
    #     return redirect("list_objectives")

class ObjectivesUpdateView(LoginRequiredMixin, UpdateView):
    model = Objective
    template_name = "objectives/edit.html"
    fields = ["name", "description", "due_date"]