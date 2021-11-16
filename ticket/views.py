from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render



def index(request):
    return render(request, 'ticket/index.html')


def map(request):
    return render(request, 'ticket/map.html')


def search_result(request):
    return render(request, 'ticket/searchres.html')


def categories(request):
    return render(request, '#')


def pageNotFound(request, exeption):
    return HttpResponseNotFound('Cтраница не найдена')