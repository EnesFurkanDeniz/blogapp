from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_request, name="login"),
    path("registration/", views.registration_request, name="registration"),
    path("logout/", views.logout_request, name="logout"),
]
