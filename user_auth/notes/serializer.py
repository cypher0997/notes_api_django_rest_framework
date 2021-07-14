from rest_framework import serializers
from .models import Notes


class NotesSer(serializers.ModelSerializer):
    # serializer class for Notes database
    class Meta:
        model = Notes
        fields = "__all__"


class NotesUpdateSer(serializers.ModelSerializer):
    # specific serializer class for updating notes in database
    class Meta:
        model = Notes
        fields = ["id", "title", "discription"]


