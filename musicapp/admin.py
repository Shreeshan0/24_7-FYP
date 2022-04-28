from django.contrib import admin
from .models import *
from .models import Post

# Register your models here.

admin.site.register(Song)
admin.site.register(Playlist)
admin.site.register(Favourite)
admin.site.register(Recent)
admin.site.register(Post)
admin.site.register(Comment)



