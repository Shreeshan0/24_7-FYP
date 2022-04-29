from dataclasses import field
import imp
from operator import mod
from socket import fromshare
from django import forms
from musicapp.models import Song
from django.contrib.auth.models import User
from musicapp.models import Comment


class AudioForm(forms.ModelForm):
    class Meta:
        model = Song
        fields =  ['name', 'album', 'genre', 'song_img', 'year', 'singer', 'song_file']


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class':'md-textarea form-control',
        'palceholder': 'comment here....',
        'rows': '3',
    }))

    class Meta:
        model = Comment
        fields = ('content',)

