from django import forms
from .models import Challenge

class NewChallengeForm(forms.ModelForm):
    class Meta:
        model = Challenge
        fields = ['title', 'topic', 'short_description', 'number_of_checks', 'deadline', 'challenge_text', 'notes']
