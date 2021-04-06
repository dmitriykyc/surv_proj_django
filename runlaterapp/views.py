from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from mainapp.models import Surveys
from runlaterapp.models import RunLater


@login_required
def index(request):
    page_title = 'Пройти позже'
    total_survey_later = RunLater.objects.filter(user=request.user) #Но этот же показатель считается на этой странице просто в шаблоне .count, это указано для того чтобы внести в inc_memu значение!!!!
    basket = request.user.runlater.all()
    context = {
        'page_title': page_title,
        'survey_later': basket,
        "total_survey_later": total_survey_later
    }

    return render(request, 'runalterapp/index.html', context)


@login_required
def add_run_later(request, pk):
    survey_item = RunLater.objects.filter(
        user_id=request.user,
        survey_id=pk
    ).first()

    if not survey_item:
        survey_item = RunLater.objects.create(
            user=request.user,
            survey_id=pk
        )
        survey_item.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def delete_run_later(request, pk):
    survey_item = RunLater.objects.filter(
        user=request.user,
        id=pk
    )
    if survey_item:
        survey_item.delete()
        # survey_item.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))