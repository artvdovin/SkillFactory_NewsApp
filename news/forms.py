from django.core.exceptions import ValidationError

from .models import Post
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author' , 'postCategory', 'title', 'post']



