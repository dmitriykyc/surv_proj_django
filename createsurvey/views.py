from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
 
def homePageView(request):
    title = '11'


    content = {"title": title}

    return render(request, 'createsurvey/createsurvey.html', content)