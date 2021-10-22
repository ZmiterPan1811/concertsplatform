from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

def index(request):
    return HttpResponse('Главная страница с концертами')

def categories(request, catid):
    return HttpResponse('Cтраница с категориями')

def pageNotFound(request, exeption):
    return HttpResponseNotFound('Cтраница не найдена')