from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile
from movies.models import Genre
from .forms import CreateForm, LoginForm, ProfileForm
from django.contrib.auth import get_user_model, login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def userInfo(request, user_id):
    user = get_object_or_404(get_user_model(), pk=user_id)
    context = {'user':user}
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
            return redirect('accounts:updateGenre')
    else:
        userProfileform = ProfileForm()
    context = {'userProfileform':userProfileform}
    return render(request, 'accounts/update.html', context)

@login_required
def updateGenre(request):
    if request.method == 'POST':
        genre_id_list = request.POST.get(genre_id_list)
        for genre_id in genre_id_list:
            like_genre = get_object_or_404(Genre, pk=genre_id)
            if request.user in like_genre.like_users.all():
                like_genre.like_users.remove(request.user)
            else:
                like_genre.like_users.add(request.user)
    else:
        return render(request, 'accounts/updateGenre.html')


def signin(request):
    if request.user.is_authenticated:
        return redirect('movies:main')
    else:
        if request.method == 'POST':
            userLoginform = AuthenticationForm(request, request.POST)
            if userLoginform.is_valid():
                login(request, userLoginform.get_user())
                return redirect('accounts:info', request.user.pk)
        else:
            userLoginform = AuthenticationForm()
        context = {'userLoginform':userLoginform}
        return render(request, 'accounts/signin.html', context)


@login_required
def log_out(request):
    logout(request)
    return redirect('accounts:signin')