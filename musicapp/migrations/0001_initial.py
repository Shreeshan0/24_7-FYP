# Generated by Django 4.0.3 on 2022-04-21 08:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0002_alter_profile_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('album', models.CharField(max_length=200)),
                ('genre', models.CharField(choices=[('Hiphop', 'Hiphop'), ('Classic', 'Classic'), ('Pop', 'Pop')], default='Hiphop', max_length=20)),
                ('song_img', models.FileField(upload_to='')),
                ('year', models.IntegerField()),
                ('singer', models.CharField(max_length=200)),
                ('song_file', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Recent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicapp.song')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='posts')),
                ('detail', models.TextField(max_length=300)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('likes', models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playlist_name', models.CharField(max_length=200)),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicapp.song')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Favourite',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('is_fav', models.BooleanField(default=False)),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicapp.song')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
