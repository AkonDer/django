from django.shortcuts import render, \
    get_object_or_404  # импорт функций render и get_object_or_404 из модуля django.shortcuts
from .models import Post  # импорт модели Post из текущего модуля
from django.core.paginator import Paginator


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


# Обработчик GET-запросов для отображения списка блог-постов.
def post_list(request):
    posts_list = Post.published.all()  # получение всех объектов опубликованных блог-постов
    paginator = Paginator(posts_list, 3)  # создание паджинатора с 3 блоками постов
    page_number = request.GET.get('page', 1)  # получение номера страницы из GET-запроса или установка значения по умолчанию равным 1
    posts = paginator.get_page(page_number)  # получение странницы по номеру странницы из паджинатора
    return render(request, 'blog/post/list.html',
                  {'posts': posts})  # возврат отображения со списком всех блог-постов
