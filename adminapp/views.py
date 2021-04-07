from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse


@user_passes_test(lambda x: x.is_superuser)
def index(request):
    users = get_user_model().objects.all()
    context = {
        "title": 'Привет!',
        "users": users
    }

    return render(request, 'adminapp/index.html', context)

def delete_user(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)
    user.is_active = False
    user.save()
    return HttpResponseRedirect(reverse('adminapp:index'))

