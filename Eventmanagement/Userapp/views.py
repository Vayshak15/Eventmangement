from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def user(request):
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already taken!")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already taken!")
                return redirect('register')
            else:
                user_reg=User.objects.create_user(username=username,email=email,password=password)
                user_reg.save()
                messages.success(request,"Successfully created Please login")
                return redirect('/')
        else:
            messages.info(request,"password not match!!")
            return redirect('register')

    return render(request,'signup.html')
def login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.info(request,"login successfully")
            return redirect('/')
        else:
            messages.info(request,"please register")
            return redirect('register')
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')