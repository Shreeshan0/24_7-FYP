from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views
from musicapp.views import likes

# Add URLConf
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:song_id>/', views.detail, name='detail'),
    path('mymusic/', views.mymusic, name='mymusic'),
    path('playlist/', views.playlist, name='playlist'),
    path('playlist/<str:playlist_name>/', views.playlist_songs, name='playlist_songs'),
    path('favourite/', views.favourite, name='favourite'),
    path('all_songs/', views.all_songs, name='all_songs'),
    path('recent/', views.recent, name='recent'),
    path('hiphop_songs/', views.hiphop_songs, name='hiphop_songs'),
    path('classic_songs/', views.classic_songs, name='classic_songs'),
    path('pop_songs/', views.pop_songs, name='pop_songs'),
    path('play/<int:song_id>/', views.play_song, name='play_song'),
    path('play_song/<int:song_id>/', views.play_song_index, name='play_song_index'),
    path('play_recent_song/<int:song_id>/', views.play_recent_song, name='play_recent_song'),
    path('add_music/', views.add_music, name='add_music'),
    path('update_music/<int:pk>/', views.update_music, name='update_music'),
    path('delete_music/<int:pk>/', views.delete_music, name='delete_music'),

    path('faq/', views.faq, name='faq'),
    path('dashboard/', views.dashboard, name='dashboard'),
    #password Change
    
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    # password reset

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    #socials
    path('main/', views.main, name='main'),
    path('post_upload/', views.PostUpload.as_view(), name = 'postUpload'),
    path('post/<int:pk>/', views.PostDetail.as_view(), name = "postDetail"),
    path('post/<int:pk>/update', views.PostUpdateView.as_view(), name = "postUpdate"),
    path('post/<int:pk>/delete', views.PostDeleteView.as_view(), name = "postDelete"),
    path('likes/', likes, name='likes'),

    #search filter
    path('filter/', views.filter, name='filter'),


]
if settings.DEBUG:
 urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)