from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'test': "hi"
        }
    return render(request, "menus.html", context)
