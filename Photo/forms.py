from django import forms

class PostForm(forms.Form):
    image = forms.ImageField()
    body = forms.CharField(widget=forms.Textarea)

class CommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea)
