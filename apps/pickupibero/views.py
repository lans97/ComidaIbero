from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'test': "hi"
        }
    return render(request, "menus.html", context)

def login(request):
    return render(request, "login/login.html")
