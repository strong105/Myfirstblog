from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):

    text = forms.CharField(label='')

    class Meta:
        model = Post
        fields = ('text',)


class CommentForm(forms.ModelForm):

    text_massage = forms.CharField(label='')

    class Meta:
        model = Comment
        fields = ('text_massage',)
