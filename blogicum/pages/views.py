from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def AboutView(request: HttpRequest) -> HttpResponse:
    """
    страница с описанием проекта.
    """
    return render(request, 'about.html')

def RulesView(request: HttpRequest) -> HttpResponse:
    """
    страница с правилами проекта.
    """
    return render(request, 'rules.html')