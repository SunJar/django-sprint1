from django.shortcuts import render
from django.http import Http404

posts = [
    {
        'id': 0,
        'location': 'Остров отчаянья',
        'date': '30 сентября 1659 года',
        'category': 'travel',
        'text': (
            'Наш корабль потерпел крушение. Весь экипаж утонул, '
            'а я, Робинзон Крузо, был выброшен на берег острова, '
            'который назвал островом Отчаяния.'
        ),
    },
    {
        'id': 1,
        'location': 'Остров отчаянья',
        'date': '1 октября 1659 года',
        'category': 'not-my-day',
        'text': (
            'Корабль прибило к берегу. Появилась надежда добраться '
            'до него и запастись едой и вещами. Я приободрился, '
            'хотя печаль о товарищах не покидала меня.'
        ),
    },
    {
        'id': 2,
        'location': 'Остров отчаянья',
        'date': '25 октября 1659 года',
        'category': 'not-my-day',
        'text': (
            'Ночью и днём шёл дождь, был сильный ветер. Корабль '
            'разбило в щепки. Весь день я укрывал вещи от дождя.'
        ),
    },
]


def main_page_view(request):
    """Главная страница со списком всех постов."""
    context = {'posts': list(reversed(posts))}
    return render(request, 'blog/index.html', context)


def details_of_posts(request, post_id):
    """Отрисовка поста по его ID. Если не найден — 404."""
    post = next((p for p in posts if p['id'] == post_id), None)
    if post is None:
        raise Http404('Пост не найден')
    return render(request, 'blog/detail.html', {'post': post})


def category_view(request, category_slug):
    """Страница с постами по категории."""
    return render(request, 'blog/category.html', {'category': category_slug})
