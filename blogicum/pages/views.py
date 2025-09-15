from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def about_view(request: HttpRequest) -> HttpResponse:
    """Страница с описанием проекта."""
    return render(request, 'about.html')


def rules_view(request: HttpRequest) -> HttpResponse:
    """Страница с правилами проекта."""
    return render(request, 'rules.html')
