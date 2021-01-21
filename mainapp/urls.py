from django.urls import path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.survey, name='index'),
    path('<int:pk>/', mainapp.survey, name='survey'),

]
