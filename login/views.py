from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import UserRegistrationForm
# Create your views here.
def index(request):
    return HttpResponse("Hello, World")

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}!")
            return redirect('login:login')
    
    else:
        form = UserRegistrationForm()
    return render(request, "login/register.html", {"form": form})