from django.urls import path

from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('map/', map, name='map'),
    path('searchres/', search_result, name='search'),
    path('categories/<int:catid>', categories),
]


