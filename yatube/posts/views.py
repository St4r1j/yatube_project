# from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Здесь будет главная '
                        'страница проекта Yatube')


def group_posts(request, slug):
    return HttpResponse(f'Посты сообщества {slug}')