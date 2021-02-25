from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from authapp.forms import UserLoginForm


def login(request):
    user_name = None
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
        'form': form
    }

    return render(request, 'authapp/login.html', context)


def logaut(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('mainapp:index'))
