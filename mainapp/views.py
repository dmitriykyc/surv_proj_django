from django.db.models import fields
from .forms import NameForm, new_survey, type_answer1, type_answer2


from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render

from .models import Surveys, Result, Questions
from runlaterapp.models import RunLater

import datetime
from django.urls import reverse

FORMS = ['new_survey', new_survey]



# Create your views here.
def main(request):
    page_title = 'Главная'
    # total_survey_later = RunLater.objects.filter(user=request.user) #Когда пользователь не залогинен, это ломается
    text = Surveys.objects.all()

    content = {
        "page_title": page_title,
        "text": text
    }
    print(request.resolver_match.url_name)

    return render(request, 'mainapp/index.html', content)
 
def survey(request, pk=None):

    if pk:
        print(pk)
        text = Questions.objects.filter(survey_id=pk)
        print('1')
    else: 
        print('pk не было')
        text = Questions.objects.all()

    context = {"text": text}
    return render(request, "mainapp/survey.html", context)

def get_text(request): 
    message = request.POST.get('text_answer_quesstion')
    print(message)


def create_survey(request):
    pk = 2
    print('sdfsdf')
    # if request.method == 'POST':
    #     print('11111')
    #      name = request.POST.get("your_name")
    #      return HttpResponse("<h2>Hello, {0}</h2>".format(name))

    # else:
        
    if pk == 2:
        
        submitbutton = request.POST.get("submit1")
        title_ = ''
        description_ = ''
        quantity_question_ = 0
        date_finish_ = ''
        userform = new_survey(request.POST or None)
        if userform.is_valid():
            title_ = userform.cleaned_data.get("title")
            description_ = userform.cleaned_data.get("description")
            quantity_question_ = userform.cleaned_data.get("quantity_question")
            date_finish_ = userform.cleaned_data.get("date_finish")
            day,month,year = date_finish_.split('/')
            date_finish_ = datetime.date(int(year), int(month), int(day))
            Surveys.objects.create(title=title_, description=description_, quantity_question=quantity_question_, date_finish=date_finish_)
            return HttpResponseRedirect(reverse("main"))
        context = {"form": userform, 'submitbutton': submitbutton, 'title': title_, 'description': description_, 'quantity_question': quantity_question_, 'date_finish': date_finish_}
    else:
        print('1')
        print(fields)
        userform = type_answer2()
        context = {"form": userform, 'submitbutton': submitbutton, 'title': title_, 'description': description_,
                   'quantity_question': quantity_question_, 'date_finish': date_finish_}
    print(request.resolver_match.url_name)
    return render(request, "mainapp/create_survey.html", context)
    # return HttpResponseRedirect('main')
