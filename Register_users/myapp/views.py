from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import person
# Create your views here.
def index(request):
    persons=person.objects.all()
    return render(request, 'index.html',{'persons':persons})

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        Email=request.POST['email']
        password=request.POST['password']
        re_password=request.POST['re_password']

        if password == re_password:
            if User.objects.filter(email=Email).exists():
                messages.info(request, 'Email already exists')
                return redirect('login')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exist')
                return redirect('login')
            else:
                user=User.objects.create(username=username,email=Email,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'password do not match')
            return redirect('login')
    else:
        return render(request, 'login.html')
            
    return render(request, 'login.html')