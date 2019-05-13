from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Avg
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Movie, Review, Comment
from .forms import ReviewForm, CommentForm

# Create your views here.
def main(request):
    movies = Movie.objects.annotate(score_avg=Avg('review__score')).order_by('-score_avg')[:20]
    return render(request, 'movies/main.html', {'movies': movies})

def detail(request, movie_pk):
    movie = Movie.objects.annotate(score_avg=Avg('review__score')).get(pk=movie_pk)
    form = CommentForm()
    context = {'movie': movie, 'form': form}
    return render(request, 'movies/detail.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    # 이미 리뷰를 작성한 적 있다면
    if movie in request.user.movie_set.all():
        messages.add_message(request, messages.WARNING, '이미 리뷰를 작성하셨습니다.')
        return redirect('movies:detail', movie_pk)
    else:
        if request.method == "POST":
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.movie = movie
                review.user = request.user
                review.save()
                request.user.profile.point += 100
                request.user.profile.save()
                print(request.user.profile.point)
                return redirect('movies:main')
        else:
            form = ReviewForm()
        context = {'form': form}
        return render(request, 'movies/form.html', context)

@login_required
@require_POST
def delete(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.user == review.user or request.user.is_superuser:
        review.delete()
        return redirect('movies:detail', movie_pk)
    else:
        messages.add_message(request, messages.WARNING, 'You are not a writer.')
        return redirect('movies:detail', movie_pk)

@login_required
@require_http_methods(['GET', 'POST'])
def update(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.user == review.user or request.user.is_superuser:
        if request.method == "POST":
            form = ReviewForm(request.POST, instance=review)
            if form.is_valid():
                form.save()
                return redirect('movies:detail', movie_pk)
        else:
            form = ReviewForm(instance=review)
        return render(request, 'movies/form.html', {'form': form})
    else:
        messages.add_message(request, messages.WARNING, 'You are not a writer.')
        return redirect('movies:detail', movie_pk)

@require_POST
@login_required
def create_comment(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.review = review
        comment.save()
        data = {'userPk': comment.user.pk,
                'username': comment.user.username,
                'content': comment.content,
                'reviewPk': comment.review.pk,
                'commentPk': comment.pk
                }
        return JsonResponse(data)

