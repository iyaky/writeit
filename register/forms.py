from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from challenges.models import Challenge


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    error_messages = {
        'password_mismatch': "The two password fields didn't match.",
    }

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'country', 'photo']

class CompleteChallenge(forms.ModelForm):
    class Meta:
        model = Challenge
        fields = ['peer_review_text']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Challenge
        fields = ['feedback']
