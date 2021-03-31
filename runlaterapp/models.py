from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from mainapp.models import Surveys


class RunLater(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='runlater')
    survey = models.IntegerField()

    @property
    def total(self):
        print('two')
        aaaa = "hello"
        return aaaa
