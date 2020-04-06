from django import forms
from .models import Thing, Comment

class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = [
            'title',
            'photo',
            'text',
            'tag'
        ]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'thing',
            'author',
            'text',
        ]