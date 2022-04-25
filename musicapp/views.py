from http.client import HTTPResponse
from urllib import response
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import AudioForm
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from .models import Post,Song
from itertools import chain
from django.contrib.auth import get_user_model
from django.template.loader import render_to_string
from django.http import JsonResponse
from .models import Like



# Create your views here.
def index(request):

    #Display recent songs
    if not request.user.is_anonymous :
        recent = list(Recent.objects.filter(user=request.user).values('song_id').order_by('-id'))
        recent_id = [each['song_id'] for each in recent][:5]
        recent_songs_unsorted = Song.objects.filter(id__in=recent_id,recent__user=request.user)
        recent_songs = list()
        for id in recent_id:
            recent_songs.append(recent_songs_unsorted.get(id=id))
    else:
        recent = None
        recent_songs = None

    first_time = False
    #Last played song
    if not request.user.is_anonymous:
        last_played_list = list(Recent.objects.filter(user=request.user).values('song_id').order_by('-id'))
        if last_played_list:
            last_played_id = last_played_list[0]['song_id']
            last_played_song = Song.objects.get(id=last_played_id)
        else:
            first_time = True
            last_played_song = Song.objects.get(id=1)

    else:
        first_time = True
        last_played_song = Song.objects.get(id=1)

    #Display all songs
    songs = Song.objects.all()

    #Display few songs on home page
    songs_all = list(Song.objects.all().values('id').order_by('?'))
    sliced_ids = [each['id'] for each in songs_all][:5]
    indexpage_songs = Song.objects.filter(id__in=sliced_ids)

    # Display Hiphop Songs
    songs_hiphop = list(Song.objects.filter(genre='Hiphop').values('id'))
    sliced_ids = [each['id'] for each in songs_hiphop][:5]
    indexpage_hiphop_songs = Song.objects.filter(id__in=sliced_ids)

    # Display Classic Songs
    songs_classic = list(Song.objects.filter(genre='Classic').values('id'))
    sliced_ids = [each['id'] for each in songs_classic][:5]
    indexpage_classic_songs = Song.objects.filter(id__in=sliced_ids)

    # Display Pop Songs
    songs_pop = list(Song.objects.filter(genre='Pop').values('id'))
    sliced_ids = [each['id'] for each in songs_pop][:5]
    indexpage_pop_songs = Song.objects.filter(id__in=sliced_ids)

    # Display rock Songs
    songs_rock = list(Song.objects.filter(genre='Rock').values('id'))
    sliced_ids = [each['id'] for each in songs_rock][:5]
    indexpage_rock_songs = Song.objects.filter(id__in=sliced_ids)

    if len(request.GET) > 0:
        search_query = request.GET.get('q')
        filtered_songs = songs.filter(Q(name__icontains=search_query)).distinct()
        context = {'all_songs': filtered_songs,'last_played':last_played_song,'query_search':True}
        return render(request, 'musicapp/index.html', context)

    context = {
        'all_songs':indexpage_songs,
        'recent_songs': recent_songs,
        'hiphop_songs':indexpage_hiphop_songs,
        'classic_songs':indexpage_classic_songs,
        'pop_songs':indexpage_pop_songs,
        'rock_songs':indexpage_rock_songs,
        'last_played':last_played_song,
        'first_time': first_time,
        'query_search':False,
    }
    return render(request, 'musicapp/index.html', context=context)


def hiphop_songs(request):

    hiphop_songs = Song.objects.filter(genre='Hiphop')

    #Last played song
    last_played_list = list(Recent.objects.values('song_id').order_by('-id'))
    if last_played_list:
        last_played_id = last_played_list[0]['song_id']
        last_played_song = Song.objects.get(id=last_played_id)
    else:
        last_played_song = Song.objects.get(id=1)

    query = request.GET.get('q')

    if query:
        hiphop_songs = Song.objects.filter(Q(name__icontains=query)).distinct()
        context = {'hiphop_songs': hiphop_songs}
        return render(request, 'musicapp/hiphop_songs.html', context)

    context = {'hiphop_songs':hiphop_songs,'last_played':last_played_song}
    return render(request, 'musicapp/hiphop_songs.html',context=context)


def classic_songs(request):

    classic_songs = Song.objects.filter(genre='Classic')

    #Last played song
    last_played_list = list(Recent.objects.values('song_id').order_by('-id'))
    if last_played_list:
        last_played_id = last_played_list[0]['song_id']
        last_played_song = Song.objects.get(id=last_played_id)
    else:
        last_played_song = Song.objects.get(id=1)

    query = request.GET.get('q')

    if query:
        classic_songs = Song.objects.filter(Q(name__icontains=query)).distinct()
        context = {'classic_songs': classic_songs}
        return render(request, 'musicapp/classic_songs.html', context)

    context = {'classic_songs':classic_songs,'last_played':last_played_song}
    return render(request, 'musicapp/classic_songs.html',context=context)

def pop_songs(request):

    pop_songs = Song.objects.filter(genre='Pop')

    #Last played song
    last_played_list = list(Recent.objects.values('song_id').order_by('-id'))
    if last_played_list:
        last_played_id = last_played_list[0]['song_id']
        last_played_song = Song.objects.get(id=last_played_id)
    else:
        last_played_song = Song.objects.get(id=1)

    query = request.GET.get('q')

    if query:
        pop_songs = Song.objects.filter(Q(name__icontains=query)).distinct()
        context = {'pop_songs': pop_songs}
        return render(request, 'musicapp/pop_songs.html', context)

    context = {'pop_songs':pop_songs,'last_played':last_played_song}
    return render(request, 'musicapp/pop_songs.html',context=context)

def rock_songs(request):

    rock_songs = Song.objects.filter(genre='Rock')

    #Last played song
    last_played_list = list(Recent.objects.values('song_id').order_by('-id'))
    if last_played_list:
        last_played_id = last_played_list[0]['song_id']
        last_played_song = Song.objects.get(id=last_played_id)
    else:
        last_played_song = Song.objects.get(id=1)

    query = request.GET.get('q')

    if query:
        rock_songs = Song.objects.filter(Q(name__icontains=query)).distinct()
        context = {'rock_songs': rock_songs}
        return render(request, 'musicapp/rock_songs.html', context)

    context = {'rock_songs':rock_songs,'last_played':last_played_song}
    return render(request, 'musicapp/rock_songs.html',context=context)

def faq(request):
    return render(request, 'musicapp/faq.html')

@login_required(login_url='login')
def play_song(request, song_id):
    songs = Song.objects.filter(id=song_id).first()
    # Add data to recent database
    if list(Recent.objects.filter(song=songs,user=request.user).values()):
        data = Recent.objects.filter(song=songs,user=request.user)
        data.delete()
    data = Recent(song=songs,user=request.user)
    data.save()
    return redirect('all_songs')


@login_required(login_url='login')
def play_song_index(request, song_id):
    songs = Song.objects.filter(id=song_id).first()
    # Add data to recent database
    if list(Recent.objects.filter(song=songs,user=request.user).values()):
        data = Recent.objects.filter(song=songs,user=request.user)
        data.delete()
    data = Recent(song=songs,user=request.user)
    data.save()
    return redirect('index')

@login_required(login_url='login')
def play_recent_song(request, song_id):
    songs = Song.objects.filter(id=song_id).first()
    # Add data to recent database
    if list(Recent.objects.filter(song=songs,user=request.user).values()):
        data = Recent.objects.filter(song=songs,user=request.user)
        data.delete()
    data = Recent(song=songs,user=request.user)
    data.save()
    return redirect('recent')


def all_songs(request):
    songs = Song.objects.all()
    last_played_song= None
    first_time = False
    # prod = Song.objects.filter(genre=genre)
    #Last played song
    if not request.user.is_anonymous:
        last_played_list = list(Recent.objects.filter(user=request.user).values('song_id').order_by('-id'))
        if last_played_list:
            last_played_id = last_played_list[0]['song_id']
            last_played_song = Song.objects.get(id=last_played_id)
    else:
        first_time = True
        last_played_song = Song.objects.get(id=1)

    
    # apply search filters
    qs_singers = Song.objects.values_list('singer').all()
    s_list = [s.split(',') for singer in qs_singers for s in singer]
    all_singers = sorted(list(set([s.strip() for singer in s_list for s in singer])))
    qs_genres = Song.objects.values_list('genre').all()
    all_genres = sorted(list(set([l.strip() for lang in qs_genres for l in lang])))

    
    if len(request.GET) > 0:
        search_query = request.GET.get('q')
        search_singer = request.GET.get('singers') or ''
        search_genre = request.GET.get('genres') or ''
        filtered_songs = songs.filter(Q(name__icontains=search_query)).filter(Q(genre__icontains=search_genre)).filter(Q(singer__icontains=search_singer)).distinct()
        context = {
        'songs': filtered_songs,
        'last_played':last_played_song,
        'all_singers': all_singers,
        'all_genres': all_genres,
        'query_search': True,
        }
        return render(request, 'musicapp/all_songs.html', context)

    context = {
        'songs': songs,
        'last_played':last_played_song,
        'first_time':first_time,
        'all_singers': all_singers,
        'all_genres': all_genres,
        'query_search' : False,
        }
    return render(request, 'musicapp/all_songs.html', context=context)


def recent(request):
    
    #Last played song
    last_played_list = list(Recent.objects.values('song_id').order_by('-id'))
    if last_played_list:
        last_played_id = last_played_list[0]['song_id']
        last_played_song = Song.objects.get(id=last_played_id)
    else:
        last_played_song = Song.objects.get(id=1)

    #Display recent songs
    recent = list(Recent.objects.filter(user=request.user).values('song_id').order_by('-id'))
    if recent and not request.user.is_anonymous :
        recent_id = [each['song_id'] for each in recent]
        recent_songs_unsorted = Song.objects.filter(id__in=recent_id,recent__user=request.user)
        recent_songs = list()
        for id in recent_id:
            recent_songs.append(recent_songs_unsorted.get(id=id))
    else:
        recent_songs = None

    if len(request.GET) > 0:
        search_query = request.GET.get('q')
        filtered_songs = recent_songs_unsorted.filter(Q(name__icontains=search_query)).distinct()
        context = {'recent_songs': filtered_songs,'last_played':last_played_song,'query_search':True}
        return render(request, 'musicapp/recent.html', context)

    context = {'recent_songs':recent_songs,'last_played':last_played_song,'query_search':False}
    return render(request, 'musicapp/recent.html', context=context)


@login_required(login_url='login')
def detail(request, song_id):
    songs = Song.objects.filter(id=song_id).first()

    # Add data to recent database
    if list(Recent.objects.filter(song=songs,user=request.user).values()):
        data = Recent.objects.filter(song=songs,user=request.user)
        data.delete()
    data = Recent(song=songs,user=request.user)
    data.save()

    #Last played song
    last_played_list = list(Recent.objects.values('song_id').order_by('-id'))
    if last_played_list:
        last_played_id = last_played_list[0]['song_id']
        last_played_song = Song.objects.get(id=last_played_id)
    else:
        last_played_song = Song.objects.get(id=1)


    playlists = Playlist.objects.filter(user=request.user).values('playlist_name').distinct
    is_favourite = Favourite.objects.filter(user=request.user).filter(song=song_id).values('is_fav')

    if request.method == "POST":
        if 'playlist' in request.POST:
            playlist_name = request.POST["playlist"]
            q = Playlist(user=request.user, song=songs, playlist_name=playlist_name)
            q.save()
            messages.success(request, "Song added to playlist!")
        elif 'add-fav' in request.POST:
            is_fav = True
            query = Favourite(user=request.user, song=songs, is_fav=is_fav)
            print(f'query: {query}')
            query.save()
            messages.success(request, "Added to favorite!")
            return redirect('detail', song_id=song_id)
        elif 'rm-fav' in request.POST:
            is_fav = True
            query = Favourite.objects.filter(user=request.user, song=songs, is_fav=is_fav)
            print(f'user: {request.user}')
            print(f'song: {songs.id} - {songs}')
            print(f'query: {query}')
            query.delete()
            messages.success(request, "Removed from favorite!")
            return redirect('detail', song_id=song_id)

    context = {'songs': songs, 'playlists': playlists, 'is_favourite': is_favourite,'last_played':last_played_song}
    return render(request, 'musicapp/detail.html', context=context)


def playlist(request):
    playlists = Playlist.objects.filter(user=request.user).values('playlist_name').distinct
    context = {'playlists': playlists}
    return render(request, 'musicapp/playlist.html', context=context)


def playlist_songs(request, playlist_name):
    songs = Song.objects.filter(playlist__playlist_name=playlist_name, playlist__user=request.user).distinct()

    if request.method == "POST":
        song_id = list(request.POST.keys())[1]
        playlist_song = Playlist.objects.filter(playlist_name=playlist_name, song__id=song_id, user=request.user)
        playlist_song.delete()
        messages.success(request, "Song removed from playlist!")

    context = {'playlist_name': playlist_name, 'songs': songs}

    return render(request, 'musicapp/playlist_songs.html', context=context)


def dashboard(request):
    if request.user.is_authenticated:
        user = request.user
        usersong = Song.objects.filter(user=user)
        print("sjhreshan"+str(usersong))
        context={
            'name':usersong
        }
    return render(request, 'musicapp/dashboard.html',context)



def mymusic(request):
    return render(request, 'musicapp/mymusic.html')


def add_music(request):
    
    if request.method == 'POST':
        form = AudioForm(request.POST, request.FILES or None)

        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            name1 = form.cleaned_data['album']
            name2 = form.cleaned_data['genre']
            name3 = form.cleaned_data['song_img']
            name4 = form.cleaned_data['year']
            name5 = form.cleaned_data['singer']
            name6 = form.cleaned_data['song_file']
            Song(user=usr,album=name1,genre=name2,song_img=name3,name=name,year=name4,singer=name5,song_file=name6).save()    
    else:
        form = AudioForm()
    return render(request, 'musicapp/music_add.html', {'form':form})

def update_music(request, pk):
    song = Song.objects.get(id=pk)
    form = AudioForm(instance=song)
    if request.method == 'POST':
        form = AudioForm(request.POST, instance=song)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    return render(request, 'musicapp/music_add.html', {'form':form})

def delete_music(request, pk):
    song = Song.objects.get(id=pk)
    song.delete()
    return redirect('dashboard')




def favourite(request):
    songs = Song.objects.filter(favourite__user=request.user, favourite__is_fav=True).distinct()
    print(f'songs: {songs}')
    
    if request.method == "POST":
        song_id = list(request.POST.keys())[1]
        favourite_song = Favourite.objects.filter(user=request.user, song__id=song_id, is_fav=True)
        favourite_song.delete()
        messages.success(request, "Removed from favourite!")
    context = {'songs': songs}
    return render(request, 'musicapp/favourite.html', context=context)



def main(request):
    context = {
        'posts': Post.objects.all()  
    }
    return render(request, 'socials/main.html', context)



def profile(request):
     profile = Profile.objects.get(user=request.user)
     posts = []
     aa = None
     # self posts
     profilepost = profile.user_posts()
     posts.append(profilepost)
     return render(request,'authentication/socials/profile.html',{'profile':profile,'posts':aa})



class PostListView(ListView):
    model = Post
    template_name = 'socials/main.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetail(DetailView):
    model=Post
    # template_name = 'musicapp/post_detail.html
    # 
    # ' 

class PostUpload(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['image','detail']

    
    def form_valid(self,form):
        form.instance.owner = self.request.user.profile
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['image','detail']

    def form_valid(self,form):
        form.instance.owner = self.request.user.profile
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user.profile == post.owner:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/main'
    def test_func(self):
        post = self.get_object()
        if self.request.user.profile == post.owner:
            return True
        return False

@login_required
def like_unlike_post(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Post.objects.get(id=post_id)
        profile = Profile.objects.get(user=user)

        if profile in post_obj.likes.all():
            post_obj.likes.remove(profile)
        else:
            post_obj.likes.add(profile)

        like, created = Like.objects.get_or_create(user=profile, post_id=post_id)

        if not created:
            if like.value=='Like':
                like.value='Unlike'
            else:
                like.value='Like'
        else:
            like.value='Like'

            post_obj.save()
            like.save()
            
    context = {
        'bool':True
    }

    return JsonResponse(context)

    
    

def filter(request):

    aa = request.GET['x']
    print(aa)
    uu = Song.objects.filter(genre=aa)
    t = render_to_string('ajax/all_songs.html',
        {
            'uu':uu,
        })
    return JsonResponse({'data':t})