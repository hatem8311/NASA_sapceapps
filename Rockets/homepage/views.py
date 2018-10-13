from django.shortcuts import render,redirect
from homepage.models import Rockets_time_table
def rockets(request):
    rockets= Rockets_time_table.objects.all()
    args={'rockets':rockets}
    return render(request, 'homepage/home.html',args)

def spaceports(request):
    return render(request,'homepage/spaceports.html')    




# Create your views here.
