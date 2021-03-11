from django.urls import path
import runlaterapp.views as runlaterapp

app_name = 'runlaterapp'

urlpatterns = [
    path('', runlaterapp.index, name='index'),
    path('add/<int:pk>/', runlaterapp.add_product, name='add_product'),
]
