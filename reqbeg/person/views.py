from django.shortcuts import render
from .models import Person
from django.http import HttpResponse
def leaders(request):
	List = Person.objects.all().order_by('name')
	return render(request,'person/person_list.html',{'list':List})	
#def person_details(request):
#	return render(request, 'person/person_details.html')
# Create your views here.of_people
def abc(request,slug):
	
	p = Person.objects.get(slug = slug)
	return render(request, 'person/person_details.html',{'person': p})