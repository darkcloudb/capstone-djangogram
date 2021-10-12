from django import forms
# from django.forms.fields import CharField, IntegerField


class EditBioForm(forms.Form):
    bio = forms.CharField(max_length=200)
    age = forms.IntegerField()
    email = forms.EmailField()
