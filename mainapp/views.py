from django.db.models import fields
from .forms import NameForm, new_survey, type_answer1, type_answer2


from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render

from .models import Surveys, Result, Questions

import datetime
from django.urls import reverse

FORMS = ['new_survey', new_survey]



# Create your views here.
def main(request):
    title = 'Главная'

    text = Surveys.objects.all()

    content = {"title": title, "text": text}

    return render(request, 'mainapp/index.html', content)
 
def survey(request, pk=None):

    if pk:
        print(pk)
        text = Questions.objects.filter(survey_id=pk)
        print('1')
    else: 
        print('pk не было')
        text = Questions.objects.all()

    content = {"text": text}
    return render(request, "mainapp/survey.html", content)

def get_text(request): 
    message = request.POST.get('text_answer_quesstion')
    print(message)


def print_form(request):
    pk = 2
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
            result = Surveys(title=title_, description=description_, quantity_question=quantity_question_, date_finish=date_finish_)
            result.save()
            return HttpResponseRedirect(reverse("main"))
        context = {"form": userform, 'submitbutton': submitbutton, 'title': title_, 'description': description_, 'quantity_question': quantity_question_, 'date_finish': date_finish_}
    else:
        print('1')
        print(fields)
        userform = type_answer2()
    
    return render(request, "mainapp/hhh.html", context)
    # return HttpResponseRedirect('main')
