from django import forms

class PostForm(forms.Form):
    image = forms.ImageField()
    body = forms.CharField(widget=forms.Textarea)

class CommentForm(forms.Form):
    body = forms.CharField(widget=forms.Textarea)
