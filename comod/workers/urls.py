from django.urls import path

from .views import *

urlpatterns = [
    path('workers/', workers, name='table'),
]