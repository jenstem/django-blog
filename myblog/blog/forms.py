from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    '''
    A form for submitting comments on blog posts.

    Meta class:
        model (Comment): The Comment model to be used for the form.
        fields (tuple): The fields to be included in the form.
    '''
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')