from rest_framework import serializers
from .models import Note


class NoteModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Note
        fields = ("id","title", "created", "note")