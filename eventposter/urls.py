
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from ticket.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ticket.urls')),
]

handler404 = pageNotFound

