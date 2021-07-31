from django.shortcuts import render
from django.http import HttpResponse
from .models import person
# Create your views here.
def index(request):
    persons = person.objects.all()
    return render(request, 'index.html',{'persons':persons})