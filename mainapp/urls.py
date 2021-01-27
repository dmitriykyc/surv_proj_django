from django.urls import path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.main, name='index'),
    path('<int:pk>/', mainapp.survey, name='survey'),
    path('create_survey/', mainapp.create_survey, name='create_survey'),

]
