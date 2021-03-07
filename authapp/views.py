from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from authapp.forms import UserLoginForm, UserRegistrationForm, UserUpdateForm


def login(request):
    page_title = 'Вход'
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)

                return HttpResponseRedirect(reverse('mainapp:index'))


    else:
        form = UserLoginForm()
    context = {
        'form': form,
        'page_title': page_title
    }

    return render(request, 'authapp/login.html', context)


def logaut(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


def register (request):
    page_title = 'Регистрация'
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = UserRegistrationForm()
    context = {
        'form': form,
        'page_title': page_title
    }

    return render(request, 'authapp/registration.html', context)


def update(request):
    page_title = 'Редактирование пользователя'
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = UserUpdateForm(instance=request.user)
    context = {
        'form': form,
        'page_title': page_title
    }

    return render(request, 'authapp/update.html', context)