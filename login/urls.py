from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

app_name = 'login'

urlpatterns = [
    path('', auth_view.LoginView.as_view(template_name='login/login.html'), name = "login"),
    path('register/', views.register, name ="register"),
    path('logout/', auth_view.LogoutView.as_view(template_name ='login/logout.html'), name ="logout"),

]