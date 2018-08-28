from django.urls import re_path
from notesapi.views import NotesApiList

urlpatterns = [
    re_path('^note/(?P<id>\d+)?$', NotesApiList.as_view(), name='notes_api'),
]

