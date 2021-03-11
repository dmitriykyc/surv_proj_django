from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from runlaterapp.models import RunLater


def index(request):
    pass


def add_product(request, pk):
    # print(request.user.runlater_set.filter(survey=pk).first)это посмотреть и понять как работает
    survey_item = RunLater.objects.filter(
        user=request.user,
        survey=pk
    ).first()
    if not survey_item:
        survey_item = RunLater.objects.create(
            user=request.user,
            survey=pk
        )
        survey_item.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
