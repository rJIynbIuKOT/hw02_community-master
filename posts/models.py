from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Group(models.Model):
    title = models.CharField('Название', max_length=200)
    slug = models.SlugField('Slug', unique=True)
    description = models.TextField('Описание')

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class Post(models.Model):
    text = models.TextField("Текст записи")
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, blank=True, null=True, related_name='posts')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
        ordering = ["-pub_date"]