from django.shortcuts import render,redirect
from django.http import HttpResponse as Http
from homepage.models import Rockets_time_table,major_spaceports

def rockets(request):
    rockets= Rockets_time_table.objects.all().order_by('id')
    args={'rockets':rockets}
    return render(request, 'homepage/home.html',args)

def spaceports(request):
    spaceports=major_spaceports.objects.all()
    args={ 'spaceports':spaceports}
    return render(request,'homepage/spaceports.html' , args)
