# Generated by Django 2.2 on 2021-02-24 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст вопроса')),
                ('type_answer', models.IntegerField(default=1, verbose_name='Какой тип вопроса (1 - строка, 2 - один ответ, 3 - несколько ответов)')),
                ('var_answer1', models.TextField(verbose_name='1 вариант')),
                ('var_answer2', models.TextField(blank=True, verbose_name='2 вариант')),
                ('var_answer3', models.TextField(blank=True, verbose_name='3 вариант')),
                ('var_answer4', models.TextField(blank=True, verbose_name='4 вариант')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.CreateModel(
            name='Surveys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='Заголовок опроса')),
                ('description', models.TextField(blank=True, verbose_name='Описание опроса')),
                ('quantity_question', models.IntegerField(default=0, verbose_name='Количество вопросов')),
                ('date_start', models.DateField(auto_now_add=True)),
                ('date_finish', models.DateField()),
            ],
            options={
                'verbose_name': 'Опрос',
                'verbose_name_plural': 'Опросы',
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.CharField(max_length=64, verbose_name='ID пользователя')),
                ('answer1', models.TextField(verbose_name='Вернувшийся с формы ответ на вопрос 1')),
                ('answer2', models.TextField(blank=True, verbose_name='Вернувшийся с формы ответ на вопрос 1')),
                ('answer3', models.TextField(blank=True, verbose_name='Вернувшийся с формы ответ на вопрос 1')),
                ('answer4', models.TextField(blank=True, verbose_name='Вернувшийся с формы ответ на вопрос 1')),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Questions', verbose_name='Номер вопроса')),
                ('survey_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Surveys', verbose_name='Номер опроса')),
            ],
            options={
                'verbose_name': 'Результат',
                'verbose_name_plural': 'Результаты',
            },
        ),
        migrations.AddField(
            model_name='questions',
            name='survey_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Surveys', verbose_name='Номер опроса'),
        ),
    ]
