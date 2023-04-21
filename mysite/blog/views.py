from django.shortcuts import render, \
    get_object_or_404  # импорт функций render и get_object_or_404 из модуля django.shortcuts
from .models import Post  # импорт модели Post из текущего модуля


# Определение функции post_detail с пятью аргументами: request, year, month, day, и post.
def post_detail(request, year, month, day, post):
    # Получение объекта Post или возврат ошибки 404, если объект не найден.
    # Условия для поиска объекта: опубликован, с указанным слагом (post), и датой публикации (year, month, day).
    post = get_object_or_404(Post,
                             status=Post.Status.PUBLISHED,
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)

    # Рендеринг шаблона detail.html с переданным объектом post в контексте.
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})


def post_list(request):
    """
    Функция отображения списка всех блог-постов

    Аргументы:
    request -- объект запроса

    Возвращает:
    Отображение со списком всех блог-постов
    """
    posts = Post.published.all()  # получение всех объектов опубликованных блог-постов
    return render(request, 'blog/post/list.html', {'posts': posts})  # возврат отображения со списком всех блог-постов
