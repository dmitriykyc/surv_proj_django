from django.urls import path
import runlaterapp.views as runlaterapp

app_name = 'runlaterapp'

urlpatterns = [
    path('', runlaterapp.index, name='index'),
    path('add/<int:runlater_pk>/', runlaterapp.add_run_later, name='add_run_later'),
    path('del/<int:delete_pk>/', runlaterapp.delete_run_later, name='delete_run_later'),
]
