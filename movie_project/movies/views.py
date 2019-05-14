from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Avg
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseBadRequest
from .models import Movie, Review, Comment
from .forms import ReviewForm, CommentForm

# Create your views here.
def main(request):
    movies = Movie.objects.annotate(score_avg=Avg('review__score')).order_by('-score_avg')[:20]
    # 리뷰 작성 여부 확인
    user_movies = request.user.review_set.values_list('movie__id', flat=True)
    context = {'movies': movies, 'user_movies': user_movies}
    return render(request, 'movies/main.html', context)

def detail(request, movie_pk):
    movie = Movie.objects.annotate(score_avg=Avg('review__score')).get(pk=movie_pk)
    reviewed = False
    user_movies = request.user.review_set.values_list('movie__id', flat=True)
    if movie_pk in user_movies:
        reviewed = True
    form = CommentForm()
    context = {'movie': movie, 'form': form, 'reviewed': reviewed}
    return render(request, 'movies/detail.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    # 리뷰 작성 여부 확인
    user_movies = request.user.review_set.values_list('movie__id', flat=True)
    if movie.pk in user_movies:
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
                return redirect('movies:detail', movie_pk)
        else:
            form = ReviewForm()
        context = {'form': form, 'movie': movie}
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
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = get_object_or_404(Review, pk=review_pk)
    if request.user == review.user or request.user.is_superuser:
        if request.method == "POST":
            form = ReviewForm(request.POST, instance=review)
            if form.is_valid():
                form.save()
                return redirect('movies:detail', movie_pk)
        else:
            form = ReviewForm(instance=review)
        return render(request, 'movies/form.html', {'form': form, 'movie': movie})
    else:
        messages.add_message(request, messages.WARNING, 'You are not a writer.')
        return redirect('movies:detail', movie_pk)

@require_POST
@login_required
def create_comment(request, movie_pk, review_pk):
    print(request.POST)
    if request.is_ajax():
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
                    'moviePk' : movie_pk,
                    'reviewPk': review_pk,
                    'commentPk': comment.pk,
                    }
            return JsonResponse(data)
    else:
        return HttpResponseBadRequest

@require_POST
@login_required
def delete_comment(request, comment_pk):
    if request.is_ajax():
        comment = get_object_or_404(Comment, pk=comment_pk)
        movie_pk = comment.review.movie.pk
        if request.user == comment.user or request.user.is_superuser:
            comment.delete()
            return redirect('movies:detail', movie_pk)
        else:
            messages.add_message(request, messages.WARNING, 'You are not a writer.')
            return redirect('movies:detail', movie_pk)
    else:
        return HttpResponseBadRequest

@login_required
@require_POST
def update_comment(request, comment_pk):
    if request.is_ajax():
        comment = get_object_or_404(Comment, pk=comment_pk)
        movie_pk = comment.review.movie.pk
        if request.user == comment.user or request.user.is_superuser:
            form = CommentForm(request.POST, instance=comment)
            if form.is_valid():
                print('valid')
                comment = form.save(commit=False)
                # comment.user = request.user
                # review = get_object_or_404(Review, pk=review_pk)
                # comment.review = review
                comment.save()
                data = {'userPk': comment.user.pk,
                        'username': comment.user.username,
                        'content': comment.content,
                        'moviePk' : comment.review.movie.pk,
                        'reviewPk': comment.review.pk,
                        'commentPk': comment.pk,
                        }
                return JsonResponse(data)
            print('hi')
            return JsonResponse({'error': str(form)})
        else:
            messages.add_message(request, messages.WARNING, 'You are not a writer.')
            return redirect('movies:detail', movie_pk)
    else:
        return HttpResponseBadRequest

