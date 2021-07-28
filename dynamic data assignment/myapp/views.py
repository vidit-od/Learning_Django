from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    context ={
        'name':'vidit',
        'age':19,
    }
    return render(request, 'index.html',context)
