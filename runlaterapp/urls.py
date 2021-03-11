from django.urls import path
import runlaterapp.views as runlaterapp

app_name = 'runlaterapp'

urlpatterns = [
    path('', runlaterapp.index, name='index')
]
