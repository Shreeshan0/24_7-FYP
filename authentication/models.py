from tkinter import Image
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

#models for socials 
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default = 'profile_pics\default.png', upload_to='profile_pics')
    bio = models.TextField(default="wasssup")

    def __str__(self):
        return str(self.user.username)
    
    def user_posts(self):
        return self.post_set.all()
    
    def save(self):
        super().save()
        
        img = Image.open(self.image.path)
        
        if img.height > 200 or img.width > 200:
            output_size = (200,200)
            img.thumbnail(output_size)
            img.save(self.image.path)
