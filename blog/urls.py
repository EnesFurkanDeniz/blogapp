from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("anasayfa/", views.index, name="anasayfa"),
    path("blogs/", views.blogs, name="bloglar"),
    path("blogs/<slug:slug>", views.details, name="details"),
    path("categories/<slug:slug>", views.edu_by_category, name="edu_by_category"),
    path("education/", views.education, name="egitimler"),
    path("education/<slug:slug>", views.educationDetails, name="detailsEdu")

]
