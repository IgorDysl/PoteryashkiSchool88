from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Thing(models.Model):
    id = models.IntegerField('id', primary_key=True, blank=True)
    title = models.CharField('Название', max_length=100)
    photo = models.FileField('Фото', blank=True)
    text = models.TextField('Описание')
    tag = models.CharField('Тег', blank=True, max_length=100)
    date = models.DateTimeField(default=timezone.now)
    add = models.BooleanField('Добавлять', default=True)

    def __str__(self):
        return f'{self.title} {self.add}'


    class Meta:
        verbose_name = "Предмет"
        verbose_name_plural = "Предметы"

class Comment(models.Model):
    thing = models.ForeignKey(Thing, on_delete = models.CASCADE)
    #author = models.CharField('Автор', max_length=50)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    text = models.CharField('Текст', max_length=50)

    def __str__(self):
        return f'{self.author}'

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"