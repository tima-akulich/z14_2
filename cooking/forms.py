from django import forms

from cooking.models import Recipe


class MyFirstForm(forms.Form):
    username = forms.CharField()
    age = forms.IntegerField(min_value=1, max_value=100)
    # date = forms.DateField()

    def clean_username(self):
        username = self.cleaned_data['username']
        if username == 'bad_word':
            raise forms.ValidationError('Your username has bad word')
        return username

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data


class RecipeForm(forms.Form):
    title = forms.CharField()
    text =  forms.CharField(widget=forms.Textarea(attrs={'width':"35px", 'cols' : "30px", 'rows': "10px", }))
    level = forms.IntegerField(min_value=1, max_value=100)
