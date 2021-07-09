from rest_framework import serializers
from .models import Notes


class NotesSer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = "__all__"


class NotesUpdateSer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ["id", "title", "discription"]


