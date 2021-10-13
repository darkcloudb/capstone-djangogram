from django import forms
from .models import Vid


class Vid_Form(forms.ModelForm):
    class Meta:
        model= Vid
        fields= ['username', 'vid_file']
