from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from notes.models import Notes
from .serializers import NoteSerializer


class NotesApiList(APIView):
    """ Notes """

    permission_classes = [permissions.AllowAny, ]

    def get(self, request, id):
        if id:
            try:
                notes = (Notes.objects.get(id=id),)
            except Notes.DoesNotExist:
                return Response({'status': 'No such note: %s' % id})
        else:
            notes = Notes.objects.all()
        serializer = NoteSerializer(notes, many=True)
        return Response({'data': serializer.data})

    def post(self, request, id):
        if id:
            try:
                note = NoteSerializer(data=request.data)
                if note.is_valid() and len(note.validated_data) > 0:    # updating
                    notes = Notes(id=id, **note.validated_data)
                    notes.unique_symbols = notes.calc_uniq_symbols(note.validated_data['text'])
                    notes.save()
                    return Response({'status': 'applied'})
                elif len(note.data) == 0:   # deleting
                    notes = Notes.objects.get(id=id)
                    notes.delete()
                    return Response({'status': 'applied'})
                else:
                    return Response({'status': 'Not Valid'})
            except Notes.DoesNotExist:
                return Response({'status': 'No such note: %s' % id})
        else:
            note = NoteSerializer(data=request.data)    # inserting
            if note.is_valid() and len(note.validated_data) > 0:
                note.save(unique_symbols=Notes.calc_uniq_symbols(text=note.validated_data['text']))
            else:
                return Response({'status': 'Not Valid'})
            return Response({'status': 'applied'})


