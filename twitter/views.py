from django.contrib.auth import login
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView, ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Tweet
from django.contrib.auth.models import AbstractUser

# Create your views here.

class Home(LoginRequiredMixin, ListView):
    login_url = ''
    template_name = "twitter/home.html"
    raise_exception = True
    permission_denied_message = "You are not allowed here"
    model = Tweet
    queryset = Tweet.objects.all()

class Profile(LoginRequiredMixin, View):
    template_name = 'twitter/profile.html'
    raise_exception = True
    permission_denied_message = "Page Not Found"

    def get(self, request):
        return render (request, self.template_name)
    

class Explore(ListView):
    template_name ='twitter/explore.html'
    explore = Tweet.objects.all()
    context_object_name = explore
