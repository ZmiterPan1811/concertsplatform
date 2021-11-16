from django.contrib import admin

from .models import *


admin.site.register(Category)
admin.site.register(Concert)
admin.site.register(Show)
admin.site.register(Party)


admin.site.site_title = 'Админ-панель сайта по реализации билетов'
admin.site.site_header = 'Админ-панель сайта по реализации билетов'