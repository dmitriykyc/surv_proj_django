from django.shortcuts import render

def print_form(request):

    context = {'page_title': 'Создать опрос'}

    return render(request, 'create_survey_app/createsurvey.html', context)

