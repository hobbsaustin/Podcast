from django.contrib.auth import authenticate, logout, login as auth_login
from django.shortcuts import render, redirect

from . import forms


def index(request):
    return render(request, 'homepage/index.html')

def logout_view(request):
    logout(request)
    return redirect ("/")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('/')
        else:
            return render(request, 'homepage/login.html', {'error_message': 'Invalid Login'})
    else:
        return render(request, 'homepage/login.html')

def register(request):
    form = forms.UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)

                return render(request, 'homepage/index.html')
                context = {
                    "form": form,
                }
    return render(request, 'homepage/homepage_form.hmtl', context)