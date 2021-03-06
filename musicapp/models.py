from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from requests import post
from authentication.models import Profile
from django.utils import timezone
from django.urls import reverse
from .models import *
# from musicapp.validators import validate_is_audio


# Create your models here.
class Song(models.Model):

    Genre_Choice = (
              ('Hiphop', 'Hiphop'),
              ('Classic', 'Classic'),
              ('Pop', 'Pop'),
              ('Rock', 'Rock'),
          )
    
    name = models.CharField(max_length=200)
    album = models.CharField(max_length=200)
    genre = models.CharField(max_length=20,choices=Genre_Choice,default='Hiphop')
    song_img = models.FileField()
    year = models.IntegerField()
    singer = models.CharField(max_length=200)
    song_file = models.FileField()
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True
    
    
    )

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
    likes = models.ManyToManyField(Profile, blank=True, related_name='likes')

    def str(self):
        return self.detail

    def get_absolute_url(self):
        return reverse('postDetail', kwargs={'pk': self.pk})
    
    
    def get_likes(self):
        return self.likes.count()

LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)

class Like(models.Model): 
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, max_length=8)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user}-{self.post}-{self.value}"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.user.username

    
    

