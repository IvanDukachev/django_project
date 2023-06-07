from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path("", views.startpage, name="startpage"),
    path("login_user", views.loginUser, name="loginUser"),
    path("register_user", views.registerUser, name="registerUser"),
    path("register_user", views.printData, name="printData"),
]
