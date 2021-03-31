from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from runlaterapp.models import RunLater

@login_required
def index(request):
    page_title = 'Пройти позже'
    basket = request.user.runlater.all()
    context = {
        'page_title': page_title,
        'survey_later': basket
    }

    return render(request, 'runalterapp/index.html', context)

@login_required
def add_product(request, pk):
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
