from . import views
from django.urls import path

app_name = 'twitter'

urlpatterns = [
    path('home', views.Home.as_view(), name = 'home'),
    path('profile', views.Profile.as_view(), name = 'profile'),
    path('explore', views.Explore.as_view(), name = "explore")
]