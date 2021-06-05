from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def user_register(request):
    return render(request,'register.html')

def user_login(request):
    return render(request,'login.html')
    # return HttpResponse("hello login page")