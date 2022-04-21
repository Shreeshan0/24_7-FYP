import imp
from operator import mod
from socket import fromshare
from django import forms
from musicapp.models import Song
from django.contrib.auth.models import User

class AudioForm(forms.ModelForm):
    class Meta:
        model = Song
        fields =  ['name', 'album', 'genre', 'song_img', 'year', 'singer', 'song_file','author']




