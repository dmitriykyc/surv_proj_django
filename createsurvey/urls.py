from django.urls import path
import createsurvey.views as mainapp

app_name = 'createsurvey'

urlpatterns = [
    path('', mainapp.homePageView, name='index'),
]