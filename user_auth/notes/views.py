from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView

from notes.models import Notes
from notes.serializer import NotesSer, NotesUpdateSer
from rest_framework.response import Response
from django.contrib.auth.models import User


class CreateNotes(APIView):

    def get(self, request,):
        try:
            usr_id = request.GET.get("id")
            data = Notes.objects.filter(notes_user=usr_id)
            ser = NotesSer(data, many=True)
            return Response({"data": {"note-list": ser.data}}, status=200)
        except Exception as e:
            return Response({"message": e.args})

    def post(self, request):
        try:
            usr_id = request.data.get("id")
            n_u = User.objects.get(id=usr_id)
            if n_u is None:
                raise Exception
            new_note = Notes(notes_user=n_u, title=request.data.get("title"),
                             discription=request.data.get("discription"))
            ser = NotesSer(new_note)
            neo_ser = NotesSer(data=ser.data)
            neo_ser.is_valid()
            neo_ser.save()
            print(n_u)
            return Response({"message": "NOTES CREATED"}, status=200)
        except Exception as e:
            return Response({"message": e.args})

    def put(self, request, pk):
        try:
            input_id = pk
            data = Notes.objects.get(pk=input_id)
            ser = NotesUpdateSer(data, data=request.data)
            if ser.is_valid():
                ser.save()
                return Response({"message": "USER UPDATED SUCCESSSFULLY"})
            return Response(ser.errors)
        except Exception as e:
            return Response({"message": e.args})

    def delete(self, request, pk):
        try:
            input_id = pk
            data = Notes.objects.get(pk=input_id)
            data.delete()
            return Response({"message": "NOTE SUCCESSFULLY DELETED"})
        except Exception as e:
            return Response({"message": e.args})