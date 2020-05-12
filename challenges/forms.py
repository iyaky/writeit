from django import forms
from .models import Challenge
from django.forms.widgets import CheckboxSelectMultiple
from functools import partial
DateInput = partial(forms.DateInput, {'class': 'datepicker'})

class PlainTextChallengeForm(forms.ModelForm):
    deadline = forms.DateTimeField(widget = DateInput(format='%Y-%m-%d'),
                                   input_formats=('%Y-%m-%d',))
    class Meta:
        model = Challenge
        fields = ['title', 'topic', 'short_description', 'number_of_checks', 'deadline', 'challenge_text', 'notes']

class FileChallengeForm(forms.ModelForm):
    deadline = forms.DateTimeField(widget = DateInput(format='%Y-%m-%d'),
                                   input_formats=('%Y-%m-%d',))
    class Meta:
        model = Challenge
        fields = ['title', 'topic', 'short_description', 'number_of_checks', 'deadline', 'uploaded_file', 'notes']

class FilterForm(forms.ModelForm):
    class Meta:
        model = Challenge
        fields = ['topic', 'number_of_checks', 'deadline']
