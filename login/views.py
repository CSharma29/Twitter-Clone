from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import UserRegistrationForm
from django.views.generic import View
# Create your views here.
def index(request):
    return HttpResponse("Hello, World")

class Register(View):
    from_class = UserRegistrationForm
    template_name = "login/register.html"
    
    def get(self, request):
        form = self.from_class()
        return render(request,self.template_name, {'form':form})
    
    def post(self, request):
        form = self.from_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}!")
            return redirect('login:login')
        return render(request, self.template_name, {'form':form})
