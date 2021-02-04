from django.db import models


    
class Surveys(models.Model):
    title = models.TextField(verbose_name='Заголовок опроса')
    description = models.TextField(verbose_name='Описание опроса', blank=True)
    quantity_question = models.IntegerField(verbose_name='Количество вопросов', default=0)
    date_start = models.DateField(auto_now_add=True)
    date_finish = models.DateField()

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'

    def __str__(self):
        return f'Опрос: {self.title}'
    


class Questions(models.Model):
    survey_id = models.ForeignKey(Surveys, verbose_name="Номер опроса", on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Текст вопроса')
    type_answer = models.IntegerField(verbose_name='Какой тип вопроса (1 - строка, 2 - один ответ, 3 - несколько ответов)', default=1)
    # Далее один обязательный ответ, и остальные при необходимости будут заполняться
    var_answer1 = models.TextField(verbose_name='1 вариант')
    var_answer2 = models.TextField(verbose_name='2 вариант', blank=True)
    var_answer3 = models.TextField(verbose_name='3 вариант', blank=True)
    var_answer4 = models.TextField(verbose_name='4 вариант', blank=True)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = "Вопросы"

    def __str__(self):
        return f'Вопрос {self.text} ({self.survey_id.title})'
    


class Result(models.Model):
    id_user = models.CharField(verbose_name='ID пользователя', max_length=64, unique=False)
    survey_id = models.ForeignKey(Surveys, verbose_name="Номер опроса", on_delete=models.CASCADE)
    question_id = models.ForeignKey(Questions, verbose_name="Номер вопроса", on_delete=models.CASCADE)
    answer1 = models.TextField(verbose_name='Вернувшийся с формы ответ на вопрос 1')
    answer2 = models.TextField(verbose_name='Вернувшийся с формы ответ на вопрос 1', blank=True)
    answer3 = models.TextField(verbose_name='Вернувшийся с формы ответ на вопрос 1', blank=True)
    answer4 = models.TextField(verbose_name='Вернувшийся с формы ответ на вопрос 1', blank=True)

    class Meta:
        verbose_name = "Результат"
        verbose_name_plural = 'Результаты'

    def __str__(self):
        return f'Результат: {self.id_user}'

