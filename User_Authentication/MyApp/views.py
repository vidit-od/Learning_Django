from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth,User
from django.contrib import messages
from .models import data
# Create your views here.
def index(request):
    datas= data.objects.all()
    return render(request, 'index.html',{'datas':datas})

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Details')
            return redirect('login')
        
    return render(request, 'login.html')

def signup(request):
    if request.method=='POST':    
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        re_password=request.POST['re_password']

        if username=='' or email=='' or password=='' or re_password=='':    
            messages.info(request, 'Empty fields not allowed')
            return redirect('signup')
        else:
            if User.objects.filter(username=username).exists():
               messages.info(request, 'this username already exists')
               return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email ID already in use')
                return redirect('signup')

            elif password != re_password:
                messages.info(request, 'password and confermation password do not match')
                return redirect('signup')

            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('login')

    return render(request, 'signup.html')

def logout(request):
    auth.logout(request)
    return redirect('/')