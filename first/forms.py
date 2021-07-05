from django import forms
from django.forms import fields, models
from .models import Comment

class TodoCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')