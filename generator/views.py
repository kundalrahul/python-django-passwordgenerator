from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.


def password(request):
    return render(request, 'generator/password.html')


def passwordgenerated(request):
    characters = list('abcdefghijklmnoqurstuvwxyz')

    length = int(request.GET.get('length', 12))
    uppercase = request.GET.get('uppercase')
    number = request.GET.get('number')
    special = request.GET.get('special')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        characters.extend(list('123456789'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*(),<>?'))

    thepassword =''

    for x in range(length):
        thepassword += random.choice(characters)
    return render(request, 'generator/passwordgenerated.html', {'password': thepassword})


def about(request):
    return render(request, 'generator/about.html')
