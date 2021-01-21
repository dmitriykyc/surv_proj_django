from mainapp.models import Questions
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms import models

class new_survey(forms.Form):
    title = forms.CharField(label='title')
    description = forms.CharField(label='description')
    quantity_question = forms.CharField(label='quantity_question')
    date_finish = forms.CharField(label='date_finish')