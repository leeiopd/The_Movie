from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile
from movies.models import Genre
from .forms import CreateForm, LoginForm, ProfileForm
from django.contrib.auth import get_user_model, login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

# Create your views here.

def userInfo(request, user_id):
    user_info = get_object_or_404(get_user_model(), pk=user_id)
    user = get_object_or_404(get_user_model(), pk=request.user.pk)
    context = {'user_info':user_info, 'user':user}
    return render(request, 'accounts/info.html', context)


def signup(request):
    if request.user.is_authenticated:
        return redirect('movies:main')
    else:
        if request.method == 'POST':
            userform = CreateForm(request.POST)
            if userform.is_valid():
                user = userform.save()
                Profile.objects.create(user=user, point=0)
                login(request, user)
                return redirect('accounts:updateProfile')
        else:
            userform = CreateForm()
        context = {'userform': userform}
        return render(request, 'accounts/signup.html', context)
        

@login_required
def updateProfile(request):
    if request.method == 'POST':
        userProfileform = ProfileForm(request.POST, instance=request.user.profile)
        if userProfileform.is_valid():
            userProfileform.save()
            return redirect('accounts:profile')
    else:
        userProfileform = ProfileForm(instance=request.user.profile)
    context = {'userProfileform':userProfileform}
    return render(request, 'accounts/profile.html', context)


@login_required
def updateGenre(request):
    user = get_object_or_404(get_user_model(), pk=request.user.pk)
    if request.method == 'POST':
        allGenre = Genre.objects.all()

        for genre in allGenre:
            if user in genre.like_users.all():
                genre.like_users.remove(user)

        like_genres = request.POST.getlist('genres')
        for genreId in like_genres:
            like_genre = get_object_or_404(Genre, pk=genreId)
            like_genre.like_users.add(user)

        user_genres = user.like_genres.all()
        print(user_genres)
        context = {'user_genres': user_genres}
        return redirect('accounts:profile')
    else:
        user_genres = user.like_genres.all()
        context = {'user_genres': user_genres}
        return render(request, 'accounts/genre.html', context)


def signin(request):
    if request.user.is_authenticated:
        return redirect('movies:main')
    else:
        if request.method == 'POST':
            userLoginform = AuthenticationForm(request, request.POST)
            if userLoginform.is_valid():
                login(request, userLoginform.get_user())
                return redirect('movies:main')
        else:
            userLoginform = AuthenticationForm()
        context = {'userLoginform':userLoginform}
        return render(request, 'accounts/signin.html', context)


@login_required
def log_out(request):
    logout(request)
    return redirect('accounts:signin')

@login_required
def subscribe(request, user_id):
    if request.is_ajax():
        User = get_user_model()
        target_user = get_object_or_404(User, pk=user_id)
        
        if request.user in target_user.subscribers.all():
            target_user.subscribers.remove(request.user)
            is_subscribe = False
        else:
            target_user.subscribers.add(request.user)
            is_subscribe = True
        return JsonResponse({'is_subscribe':is_subscribe, 'subscribe_count':target_user.subscribers.count()})


@login_required
def subscribeList(request, user_id):
    user = get_object_or_404(get_user_model(), pk=user_id)
    subscribes = user.subscribe.all()
    context = {'subscribes': subscribes}
    return render(request, 'accounts/subscribes.html', context)


@login_required
def subscriberList(request, user_id):
    user = get_object_or_404(get_user_model(), pk=user_id)
    subscribers = user.subscribers.all()
    context = {'subscribers':subscribers}
    return render(request, 'accounts/subscribers.html', context)