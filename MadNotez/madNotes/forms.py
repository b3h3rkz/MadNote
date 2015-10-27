__author__ = 'root'
from registration.forms import RegistrationForm
from django import forms


class ExRegistrationForm(RegistrationForm):
    HUMAN_CHOICES = (
        ('y', 'YES'),
        ('n', ' NO'),
    )
    is_human = forms.ChoiceField(label = "Are you human?:", choices=HUMAN_CHOICES)