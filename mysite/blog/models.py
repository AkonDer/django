from django.db import models  # импорт модуля для определения моделей базы данных
from django.utils import timezone  # импорт модуля для работы с временем
from django.contrib.auth.models import User  # импорт модели пользователя Django
from django.urls import reverse  # импорт модуля для работы с путями


class PublishedManager(models.Manager):
    # менеджер для выборки только опубликованных записей
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class Post(models.Model):
    # класс для определения возможных значений поля "status"
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    # поля модели "Post"
    title = models.CharField(max_length=250)  # заголовок блог-поста
    slug = models.SlugField(max_length=250, unique_for_date='publish')  # уникальный URL для блог-поста
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')  # автор блог-поста
    body = models.TextField()  # основной текст блог-поста
    publish = models.DateTimeField(default=timezone.now)  # дата и время публикации блог-поста
    created = models.DateTimeField(auto_now_add=True)  # дата и время создания блог-поста
    updated = models.DateTimeField(auto_now=True)  # дата и время последнего обновления блог-поста
    status = models.CharField(max_length=2, choices=Status.choices,
                              default=Status.DRAFT)  # статус блог-поста (черновик или опубликован)

    # менеджеры модели "Post"
    objects = models.Manager()  # менеджер по умолчанию
    published = PublishedManager()  # менеджер для выборки только опубликованных записей

    class Meta:
        ordering = ('-publish',)  # сортировка записей по убыванию даты публикации
        indexes = [
            models.Index(fields=['-publish']),  # индекс для ускорения запросов на выборку записей по дате публикации
        ]

    def __str__(self):
        return self.title  # возвращает название блог-поста в виде строки

    # Функция get_absolute_url используется для получения абсолютного URL-адреса поста блога
    def get_absolute_url(self):
        # Функция reverse генерирует URL на основе заданного шаблона и аргументов
        return reverse(
            'blog:post_detail',  # ссылка на маршрут с именем 'post_detail' внутри пространства имен 'blog'
            args=[
                self.publish.year,  # год публикации поста
                self.publish.month,  # месяц публикации поста
                self.publish.day,  # день публикации поста
                self.slug,  # слаг поста
            ]
        )  # возвращает абсолютный URL для блока-поста
