from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from .models import User


# Create your views here.
def index(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(
                request,
                "auctions/register.html",
                {
                    "message": "Passwords do not match",
                },
            )
    return render(request, "app/index.html")


def login_view(request):
    return render(request, "app/login.html")


def logout_view(request):
    pass


def register(request):
    return render(request, "app/register.html")
