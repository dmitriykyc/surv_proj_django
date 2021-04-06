
from django.contrib import admin
from django.urls import path
import mainapp.views as mainapp
from django.conf.urls import include
import create_survey_app.views as cr_sur

urlpatterns = [
    path('', mainapp.main, name='index'),
    path('survey/', include("mainapp.urls", namespace='survey')),
    path('auth/', include("authapp.urls", namespace='auth')),
    path('runlater/', include("runlaterapp.urls", namespace='runlater')),
    path('admin/', admin.site.urls),
    path('create_survey/', mainapp.create_survey, name='create_survey'),
    path('administration/', include('adminapp.urls'), name='administration'),
    # path('create_survey/', cr_sur.print_form, name='create_survey'), #print_form у меня пока нет((

]
