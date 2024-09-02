from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, LoginForm


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("quotes:root")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})


def login(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect("quotes:root")
    else:
        form = LoginForm()
    return render(request, "users/login.html", {"form": form})


@login_required
def logout(request):
    if request.method == "POST":
        auth_logout(request)
        return redirect("quotes:root")
