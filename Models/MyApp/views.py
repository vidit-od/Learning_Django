from django.shortcuts import render
from django.http import HttpResponse
from .models import content
# Create your views here.
def index(request):
    person1= content()
    person2=content()
    person3= content()
    person4=content()
    person5= content()
    person6=content()
    person7= content()
    person8=content()
    person9= content()
    person10=content()
    
    person1.id=1
    person1.name='person1'
    person1.job='student'

    person2.id=2
    person2.name='person2'
    person2.job='student'

    person3.id=3
    person3.name='person3'
    person3.job='student'

    person4.id=4
    person4.name='person4'
    person4.job='student'

    person5.id=5
    person5.name='person5'
    person5.job='student'

    person6.id=6
    person6.name='person6'
    person6.job='student'

    person7.id=7
    person7.name='person7'
    person7.job='student'
    
    person8.id=8
    person8.name='person8'
    person8.job='student'

    person9.id=9
    person9.name='person9'
    person9.job='student'

    person10.id=10
    person10.name='person10'
    person10.job='student'


    persons=[person1, person2, person3, person4, person5, person6, person7, person8, person9, person10]
    return render(request, 'index.html',{'persons': persons})
