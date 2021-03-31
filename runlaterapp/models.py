from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from mainapp.models import Surveys


class RunLater(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='runlater')
    survey = models.ForeignKey(Surveys, on_delete=models.CASCADE)

    @staticmethod
    def total_quant2():
        return '9999'

    # тут в пробном варианте была фишка с подсчётом суммы в корзину, тоесть логика пописана тут была, я пока не нашел что сделать, но это тут.
    # Урок 6.Корзина + AJAX + декораторы В первой половине до перерыва
    # @property
    # def total(self):
    #     print('two')
    #     aaaa = "hello"
    #     return aaaa


