from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import customLoginForm

def landing(request):
    return render(request, "menus.html")

def login_view(request):
    context = {}
    if request.user.is_authenticated:
        return redirect('landing')
    if request.method == 'POST':
        form = customLoginForm(request.POST)
        if form.is_valid():
            ncuenta = form.cleaned_data.get('ncuenta')
            digitov = form.cleaned_data.get('digitov')
            password = form.cleaned_data.get('password')

            username = str(ncuenta) + "-" + str(digitov)

            user = authenticate(request, username=username, password=password)

            if user is not None:
                # Authentication successful, log the user in
                login(request, user)
                return redirect('landing')
            else:
                # Authentication failed, handle accordingly
                form.add_error('ncuenta', 'Invalid credentials')  # Add error to the form

    else:
        form = customLoginForm()

    context['form'] = form
    return render(request, "login/login.html", context)

def logout_view(request):
    logout(request)
    next_url = request.POST.get('next') or request.GET.get('next') or 'landing'
    return redirect(next_url)
