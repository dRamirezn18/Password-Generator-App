from django.shortcuts import render
import random
# Create your views here.
def index(request):
    number = [6,7,8,9,10,11,12,13,14,15]
    context = {
        "number": number
    }
    return render(request, "index.html", context)

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    generated_pass = ''
    length = int(request.GET.get('length'))
    
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    if request.GET.get('uppercase'):
        characters.extend(list('@-_.,:¿?*()&#'))
    

    for x in range(length):
        generated_pass += random.choice(characters)

    context = {
        "password": generated_pass,
    }


    return render(request, "password.html", context)

def about(request):
    return render(request, "about.html")