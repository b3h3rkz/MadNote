from django.http import request

__author__ = 'root'
from registration.forms import RegistrationForm
from django import forms
from madNotes.models import Tags, Note
from django.http import HttpResponseRedirect, request
from django.shortcuts import render


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'note', 'tags')


class TagForm(forms.ModelForm):
    class Meta:
        model = Tags
        fields = ('slug',)


class ExRegistrationForm(RegistrationForm):
    HUMAN_CHOICES = (
        ('y', 'YES'),
        ('n', ' NO'),
    )
    is_human = forms.ChoiceField(label="Are you human?:", choices=HUMAN_CHOICES)

