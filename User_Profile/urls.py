from django.urls import path
from . import views

app_name = "User_Profile"

urlpatterns = [
    path('user_name/', views.Profile.as_view(), name ="user_name"),
    path('<pk>', views.User_DetailView.as_view(), name = "user_detail"),
    path('follow_unfollow/', views.follow_unfollow, name ="follow_unfollow_view"),
]