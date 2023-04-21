from django.contrib import admin  # импорт модуля "admin" из "django.contrib"
from .models import Post  # импорт модели "Post" из текущего модуля


@admin.register(Post)  # регистрация модели "Post" в административном интерфейсе
class PostAdmin(admin.ModelAdmin):  # определение класса настроек для модели "Post"
    list_display = ('title', 'slug', 'author', 'publish', 'status')  # отображаемые поля модели в списке записей
    list_filter = ('status', 'created', 'publish', 'author')  # поля, по которым можно фильтровать записи
    search_fields = ('title', 'body')  # поля, по которым можно осуществлять поиск
    prepopulated_fields = {'slug': ('title',)}  # автоматическое заполнение поля "slug" на основе поля "title"
    raw_id_fields = ('author',)  # поля, выбираемые из всплывающих окон выбора
    date_hierarchy = 'publish'  # группировка записей по дате
