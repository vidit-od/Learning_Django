from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'index.html')

def counter(request):
    # if we are using get methode 
    # text = request.GET['text']

    # if we re using post method
    text = request.POST['text']
    words=len(text.split())
    return render(request, 'counter.html',{'num':words})