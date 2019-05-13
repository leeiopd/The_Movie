from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile
from .forms import CreateForm, LoginForm, ProfileForm #, ChangeForm
from django.contrib.auth import get_user_model, login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def userInfo(request, user_id):
    user = get_object_or_404(get_user_model(), pk=user_id)
    context = {'user':user}
    return render(request, 'accounts/info.html', context)

def signup(request):
    if request.method == 'POST':
        userform = CreateForm(request.POST)
        if userform.is_valid():
            user = userform.save()
            Profile.objects.create(user=user, point=0)
            login(request, user)
            return redirect('accounts:update')
    else:
        userform = CreateForm()
    context = {'userform': userform}
    return render(request, 'accounts/signup.html', context)

def update(request):
    if request.method == 'POST':
        userProfileform = ProfileForm(request.POST, instance=request.user.profile)
        if userProfileform.is_valid():
            userProfileform.save()
            return redirect('accounts:info', request.user.pk)
    else:
        userProfileform = ProfileForm()
    context = {'userProfileform':userProfileform}
    return render(request, 'accounts/update.html', context)

def signin(request):
    if request.method == 'POST':
        userLoginform = AuthenticationForm(request, request.POST)
        if userLoginform.is_valid():
            login(request, userLoginform.get_user())
            return redirect('accounts:info', request.user.pk)
    else:
        userLoginform = AuthenticationForm()
    context = {'userLoginform':userLoginform}
    return render(request, 'accounts/signin.html', context)

def log_out(request):
    logout(request)
    return redirect('accounts:signin')


