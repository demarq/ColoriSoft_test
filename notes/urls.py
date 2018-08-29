from django.urls import path
from notes.views import *

urlpatterns = [
    path('', home, name='notes'),
]
