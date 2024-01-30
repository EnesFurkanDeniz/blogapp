from django.shortcuts import render
from blog.models import Blog, Category, Education


def index(request):
    data = {
        "anasayfa":Blog.objects.filter(is_active = True)
    }
    return render(request,"blog/index.html", data)

def blogs(request): 
    data = {
        "blogs":Blog.objects.all()
    }
    return render(request, "blog/blogs.html", data)

def education(request):
    data = {
        "educations" : Education.objects.all(),
        "categories" : Category.objects.all()
    }
    return render(request, "blog/education.html", data)


def details(request,slug):
    data = {
        "details": Blog.objects.get(slug=slug)
    }
    return render (request, "blog/details.html",data)


def educationDetails (request,slug):
    data = {
        "educations" : Education.objects.get(slug=slug),
    }
    return render(request, "blog/detailsEdu.html", data)

def edu_by_category (request, slug):
    data = {
        "educations" : Education.objects.filter(is_active=True, categories__slug=slug),
        "categories" : Category.objects.all()
    }
    return render(request, "blog/education.html", data)