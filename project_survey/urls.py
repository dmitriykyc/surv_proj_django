"""project_survey URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import mainapp.views as mainapp
from django.conf.urls import include
import create_survey_app.views as cr_sur

urlpatterns = [
    path('', mainapp.main, name='main'),
    path('survey/', include("mainapp.urls", namespace='survey')),
    path('admin/', admin.site.urls),
    path('hhh/', mainapp.print_form, name='print_form'),
    path('create_survey/', cr_sur.print_form, name='create_survey'), #print_form у меня пока нет((

]
