from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from mainapp.models import Surveys


class RunLater(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    survey = models.IntegerField()