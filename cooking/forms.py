from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from cooking.models import Recipe, User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username',
            'password1',
            'password2'
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        if commit:
            user.save()
        return user


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'text', 'level', 'author')

    def clean_title(self):
        val = self.cleaned_data['title']
        if not val:
            raise ValidationError('Title is empty!')
        return val

    def clean_text(self):
        val = self.cleaned_data['text']
        if not val:
            raise ValidationError('Text is empty!')
        return val
