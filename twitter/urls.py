from . import views
from django.urls import path

app_name = 'twitter'

urlpatterns = [
    path('home', views.Home.as_view(), name = 'home'),
    #path('explore', views.Explore.as_view(), name = "explore"),
    path('tweet', views.Tweet_Post.as_view(), name ="tweet"),
    path('tag/<slug:slug>/', views.tagged, name='tagged'),
]