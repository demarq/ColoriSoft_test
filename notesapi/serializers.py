from rest_framework import serializers
from notes.models import Notes


class NoteSerializer(serializers.ModelSerializer):
    """ Notes serializer """

    class Meta:
        model = Notes
        fields = ('id', 'title', 'text', 'unique_symbols')
