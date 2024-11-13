
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .forms import UserRegister, UserLogin
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout

import uuid

# Create your views here.

User = get_user_model()

def register(request):
	form = UserRegister()
	if request.method == "POST":
		form = UserRegister(request.POST)
		if form.is_valid():
			form.save()
			return redirect("login")
	context = {"register": "Register", "form": form}
	return render(request, "local_connect/register.html", context=context)

def login(request):
	form = UserLogin()
	if request.method == 'POST':
		form = UserLogin(request, data=request.POST)
		if form.is_valid():
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username=username, password=password)
			if user is not None:
				auth.login(request, user)
				return redirect('community_hub')
	context = {"login": "Login", "form": form}
	return render(request, "local_connect/login.html", context=context)


def community_hub(request):
	return render(request, "local_connect/community_hub.html")

def business_profile(request):
	return render(request, "local_connect/business-profile.html")

def view_business(request):
	return render(request, "local_connect/view-business.html")

def events(request):
	return render(request, "local_connect/events.html")

def profile(request):
	return render(request, "local_connect/profile.html")

def payments(request):

	return render(request, "local_connect/payment.html")


