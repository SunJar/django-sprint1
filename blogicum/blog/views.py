from django.shortcuts import render
from django.http import Http404


posts = [
    {
        'id': 0,
        'location': 'Остров отчаянья',
        'date': '30 сентября 1659 года',
        'category': 'travel',
        'text': (
            'Наш корабль, застигнутый в открытом море страшным штормом, '
            'потерпел крушение. Весь экипаж, кроме меня, утонул; я же, '
            'несчастный Робинзон Крузо, был выброшен полумёртвым на берег '
            'этого проклятого острова, который назвал островом Отчаяния.'
        )
    },
    {
        'id': 1,
        'location': 'Остров отчаянья',
        'date': '1 октября 1659 года',
        'category': 'travel',
        'text': (
            'Только сегодня, придя в себя после тяжёлой болезни, я понял, '
            'что на острове, куда забросила меня судьба, нет ни единого '
            'человеческого существа. Душу мою наполняет ужас, но буду '
            'уповать на помощь Божию.'
        )
    },
    {
        'id': 2,
        'location': 'Остров отчаянья',
        'date': '26 октября 1659 года',
        'category': 'travel',
        'text': (
            'На следующий день после моего бегства я отправился на поиски '
            'пищи и места, где можно было бы устроиться на ночлег. Я сделал '
            'себе топор и другие орудия. '
            'Моя жизнь постепенно становится легче.'
        )
    }
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
