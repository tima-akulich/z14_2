from django import forms
from django.contrib.auth.forms import UserCreationForm

from cooking.models import Recipe, User, BaseReaction, RecipeReaction
from cooking.utils import convert_image_to_base64


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'text', 'level', 'image')

    def save(self, commit=True):
        recipe = super().save(commit=False)
        if recipe.image:
            recipe.image_base64 = convert_image_to_base64(recipe.image.file)
        else:
            recipe.image_base64 = ''

        if commit:
            recipe.save()
        return recipe


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class ReactionForm(forms.Form):
    recipe_id = forms.IntegerField()
    reaction = forms.CharField()

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.instance = kwargs.pop('instance')
        super().__init__(*args, **kwargs)

    def clean_reaction(self):
        reaction = self.cleaned_data['reaction']
        if reaction not in BaseReaction.ALL:
            raise forms.ValidationError('Invalid reaction')
        return reaction

    def save(self):
        reaction, created = RecipeReaction.objects.get_or_create(
            user=self.user,
            recipe_id=self.cleaned_data['recipe_id'],
            defaults={
                'status': self.cleaned_data['reaction']
            }
        )

        if not created and reaction.status == self.cleaned_data['reaction']:
            reaction.delete()
        elif not created:
            reaction.status = self.cleaned_data['reaction']
            reaction.save()
