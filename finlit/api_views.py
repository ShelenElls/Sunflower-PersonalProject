from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from finlit.models import Profile

# Create your views here.

class ProfileListView(LoginRequiredMixin, ListView):
    model = Profile
    template_name = "finance/list.html"

class ProfileCreateView(LoginRequiredMixin, CreateView):
    model = Profile
    template_name = "finance/create.html"
    fields = ["income", "expenses", "name",]

    def form_valid(self, form):
        item = form.save(commit=False)
        item.owner = self.request.user
        item.save()
        return redirect("list_finance")


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = "finance/edit.html"
    fields = ["income", "expenses", "name"]
    success_url = reverse_lazy("list_finance")