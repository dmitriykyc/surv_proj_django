from django.contrib.auth.models import User, AbstractUser
from django.db import models


class SurveyUser(AbstractUser):
    age = models.PositiveIntegerField('Возраст', default=10)
    avatar = models.ImageField(upload_to='avatars', blank=True)
