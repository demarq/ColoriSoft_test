from django.urls import path
from notes.views import *

urlpatterns = [
    path('notes/', home, name='notes'),
]
