from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from notes.models import Notes
from notes.serializer import NotesSer, NotesUpdateSer
from rest_framework.response import Response
from django.contrib.auth.models import User


class CreateNotes(APIView):

    # this class represent different views that are broadly different operations performed vis this api

    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)

    def get(self, request):
        """
        this method presents various notes of corresponding user
        :param request: http request to made to this api
        :return: it returns response to request that is made
        """
        try:
            usr_id = request.GET.get("id")
            data = Notes.objects.filter(notes_user=usr_id)
            serializer = NotesSer(data, many=True)
            return Response({"data": {"note-list": serializer.data}}, status=200)
        except Exception as e:
            return Response({"message": e.args})

    def post(self, request):
        """
        this method used to create notes of corresponding user
        :param request: http request to made to this api
        :return: it returns response to request that is made
        """
        try:
            usr_id = request.data.get("id")
            user = User.objects.get(id=usr_id)
            if user is None:
                raise Exception
            new_note = Notes(notes_user=user, title=request.data.get("title"),
                             discription=request.data.get("discription"))
            serializer = NotesSer(new_note)
            deserialized_data = NotesSer(data=serializer.data)
            deserialized_data.is_valid()
            deserialized_data.save()
            print(user)
            return Response({"message": "NOTES CREATED"}, status=200)
        except Exception as e:
            return Response({"message": e.args})

    def put(self, request, pk):
        """
        this method updates specific notes of corresponding user
        :param request: http request to made to this api
        :return: it returns response to request that is made:
        :param pk: primary representing user
        """
        try:
            input_id = pk
            user = Notes.objects.get(pk=input_id)
            serializer = NotesUpdateSer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "USER UPDATED SUCCESSSFULLY"})
            return Response(serializer.errors)
        except Exception as e:
            return Response({"message": e.args})

    def delete(self, request, pk):
        """
        this method delete's specific notes of corresponding user
        :param request: http request to made to this api
        :return: it returns response to request that is made:
        :param pk: primary representing user
        """
        try:
            input_id = pk
            user = Notes.objects.get(pk=input_id)
            user.delete()
            return Response({"message": "NOTE SUCCESSFULLY DELETED"})
        except Exception as e:
            return Response({"message": e.args})
