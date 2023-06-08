from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

from storeapp.forms import UserDetailsForm


# Create your views here.
def home(request):
    return render(request, "index.html")


def register(request):
    try:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            confirm_password = request.POST['con_password']
            if password == confirm_password:
                if User.objects.filter(username=username).exists():
                    messages.info(request, "Username already taken")
                    return redirect("register")
                else:
                    user = User.objects.create_user(username=username, password=password)
                    user.save()
                    return redirect("login")
            else:
                messages.info(request, "Passwords are not matching")
                return redirect("register")
    except(ValueError, TypeError):
        messages.info(request, "Please enter the details")
    return render(request, "register.html")


def login(request):
    try:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("custredirect")
            else:
                messages.info(request, "Invalid Credentials")
                return redirect("login")
    except (ValueError, TypeError):
        messages.info(request, "Enter Username and Password")
    return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect('/')


def details(request):
    form = UserDetailsForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        messages.info(request, "Order Confirmed")
        form.save()
    return render(request, "form.html", {'form': form})


def redirect_registration(request):
    return render(request,"button.html")
