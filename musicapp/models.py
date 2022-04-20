from django.db import models
from django.contrib.auth.models import User
from authentication.models import Profile
from django.utils import timezone
from django.urls import reverse
from .models import *


# Create your models here.
class Song(models.Model):

    Genre_Choice = (
              ('Hiphop', 'Hiphop'),
              ('Classic', 'Classic'),
              ('Pop', 'Pop'),
          )
    
    name = models.CharField(max_length=200)
    album = models.CharField(max_length=200)
    genre = models.CharField(max_length=20,choices=Genre_Choice,default='Hiphop')
    song_img = models.FileField()
    year = models.IntegerField()
    singer = models.CharField(max_length=200)
    # author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    song_file = models.FileField()

    def __str__(self):
        return self.name


class Playlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    playlist_name = models.CharField(max_length=200)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)


class Favourite(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    is_fav = models.BooleanField(default=False)


class Recent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)


class Post(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts')
    detail = models.TextField(max_length=300)
    date_posted = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, blank=True, related_name='likes')

    def str(self):
        return self.detail

    def get_absolute_url(self):
        return reverse('postDetail', kwargs={'pk': self.pk})