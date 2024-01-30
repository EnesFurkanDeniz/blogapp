from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def login_request (request):
    if request.user.is_authenticated:
        return redirect("anasayfa")

    if request.method == "POST":
        username = request.POST["username"]
        userpassword = request.POST["userpassword"]
        user = authenticate(request, username = username, password = userpassword )
    
        if user is not None:
            login(request, user)
            return redirect("anasayfa")
        else:
            return render(request, 'account/login.html', {"error" : "Girdiğiniz bilgiler her hangi bir kullanıcı bilgisiyle eşleşmemektedir."})

    return render(request, 'account/login.html')

def registration_request (request):

    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        password = request.POST["userpassword"]
        repassword = request.POST["repassword"]

        if password == repassword:
            if User.objects.filter(username = username).exists():
                return render(request,'account/registration.html', {
                    "error":"girdiğiniz kullanıcı ismi zaten kullanılmaktadır.",
                    "username": username,
                    "email": email,
                    "firstname" : firstname,
                    "lastname": lastname
                })
            else:
                if User.objects.filter(email = email).exists():
                    return render(request,'account/registration.html', {"error":"girdiğiniz email zaten kullanılmaktadır."})
                else:
                    user = User.objects.create_user(username=username, email=email, first_name=firstname, last_name=lastname, password=password)    
                    user.save()
                    return redirect("login")
        else:
            return render(request, 'account/registration.html', {
                "error" : "Girdiğiniz şifreler bir biriyle eşleşmemektedir."
            })




    return render(request, 'account/registration.html')

def logout_request (request):
    logout(request)
    return redirect("anasayfa")