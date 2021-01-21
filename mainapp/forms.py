from .models import Questions
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms import models

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class type_answer1(forms.Form):
    get_answer = forms.CharField(label='answer_type1')

class new_survey(forms.Form):
    title = forms.CharField(label='Заголовок опроса')
    description = forms.CharField(label='Описание опроса')
    quantity_question = forms.IntegerField(label='Количество вопросов')
    date_finish = forms.CharField(label='Дата завершения опроса? в формате 11/10/1992')


class type_answer2(forms.Form):
    FRUIT_CHOICES= [
    ('orange', 'Oranges'),
    ('cantaloupe', 'Cantaloupes'),
    ('mango', 'Mangoes'),
    ('honeydew', 'Honeydews'),
    ]
    model = Questions
    fields = ['text']
    print(fields)
    get_answer= forms.CharField(label='What is your favorite fruit?', widget=forms.RadioSelect(choices=FRUIT_CHOICES)) 



