from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
  return render(request, 'home.html', {"home": home})

def contact(request):
  return render(request, 'contact.html', {"contact": contact})
