from django.urls import path
import runlaterapp.views as runlaterapp

app_name = 'runlaterapp'

urlpatterns = [
    path('', runlaterapp.index, name='index'),
    path('add/<int:pk>/', runlaterapp.add_run_later, name='add_run_later'),
    path('del/<int:pk>/', runlaterapp.delete_run_later, name='delete_run_later'),
]
