from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



def signup(request):
    if request.method == "POST":
        username = UserCreationForm(request.POST)
        if username.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = User.objects.create_user(
                username=username,
                password=password,
            )
            user.save()
            login(request, user)
            return redirect("home")
    else:
        username = UserCreationForm()
    context = {
        "form": username,
    }
    return render(request, "registration/signups.html", context)


def home(request):
    template_name = "home.html"
    context = {}
    return render(request, template_name, context)


# home funciton needs to be changed  for JSON and React template views 