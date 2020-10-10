from django import forms
from .models import *

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)

class BookReviewForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'comment', 'link')
