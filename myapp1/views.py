from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def user_register(request):
    if request.method =='POST':
        fname = request.POST.get('firstname')
        lname = request.POST.get('lastname')
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if pass1 != pass2:
            messages.warning(request,"Password does not match")
            return redirect('register')
        elif User.objects.filter(username=uname).exists():
            messages.warning(request,'Username already exist , please try different username')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.warning(request,'E-mail already exist , please try different email')
            return redirect('register')
        else:
            user = User.objects.create_user(first_name = fname,last_name = lname,username = uname,email = email,password = pass1)
            user.save()
            messages.success(request,'Succesfully registered')
            return redirect('_login')
    
    return render(request,'register.html')

def user_login(request):
    return render(request,'login.html')
    # return HttpResponse("hello login page")