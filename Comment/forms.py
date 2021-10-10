from django import forms
from Comment.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {
            'body': forms.TextInput(attrs={'class': 'myfieldclass'}),
        }
    # body = forms.CharField(widget=forms.Textarea)
