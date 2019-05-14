from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile
from movies.models import Genre, Review
from .forms import CreateForm, LoginForm, ProfileForm
from django.contrib.auth import get_user_model, login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

# Create your views here.

@require_http_methods(['GET'])
def userInfo(request, user_id):
    user_info = get_object_or_404(get_user_model(), pk=user_id)
    user = get_object_or_404(get_user_model(), pk=request.user.pk)
    context = {'user_info':user_info, 'user':user}
    return render(request, 'accounts/info.html', context)

@require_http_methods(['GET', 'POST'])
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
                return redirect('accounts:updateUser')
        else:
            userform = CreateForm()
        context = {'userform': userform}
        return render(request, 'accounts/signup.html', context)
        

@require_http_methods(['GET', 'POST'])
@login_required
def updateUser(request):
    if request.method == 'POST':
        userProfileform = ProfileForm(request.POST, instance=request.user.profile)
        if userProfileform.is_valid():
            userProfileform.save()
            return redirect('accounts:proflieTogenre')
    else:
        userProfileform = ProfileForm(instance=request.user.profile)
    context = {'userProfileform':userProfileform}
    return render(request, 'accounts/profile.html', context)

@login_required
def proflieTogenre(request):
    return render(request, 'accounts/profileTogenre.html')


@require_http_methods(['GET', 'POST'])
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
        context = {'user_genres': user_genres}
        return redirect('accounts:user_info', user.pk)
    else:
        user_genres = user.like_genres.all()
        context = {'user_genres': user_genres}
        return render(request, 'accounts/genre.html', context)


@require_http_methods(['GET', 'POST'])
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

@require_http_methods(['GET'])
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



def viewfeed(request, user_id):
    user = get_object_or_404(get_user_model(), pk=user_id)
    # feeds = user.subscribe.prefetch_related('review_set')
    subscribes = user.subscribe.values_list('id')
    feeds = Review.objects.filter(user_id__in=subscribes).order_by('-id')
    # feeds = []
    # for user in allSubUser:
    #     feeds.append(user.review_set.all())

    context = {'feeds': feeds}
    return render(request, 'accounts/feed.html', context)


def likeCasts(request, user_id):
    user = get_object_or_404(get_user_model(), pk=user_id)
    casts = user.like_casts.all()
    context = {'casts': casts}
    return render(request, 'accounts/casts.html', context)


def likeDirectors(request, user_id):
    user = get_object_or_404(get_user_model(), pk=user_id)
    directors = user.like_directors.all()
    context = {'directors': directors}
    return render(request, 'accounts/directors.html', context)

def sidebar(request):
    return render(request, 'accounts/accounts_base.html')