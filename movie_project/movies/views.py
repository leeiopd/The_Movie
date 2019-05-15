from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Avg
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseBadRequest
from .models import Movie, Review, Comment, Director, Cast
from .forms import ReviewForm, CommentForm

# Create your views here.
@login_required
def main(request):
    # 사용자 평점 기준 movie top10
    movies_top10 = Movie.objects.annotate(score_avg=Avg('review__score')).order_by('-score_avg')[:10]
    # themoviedb 기준 movie top10
    movies_dbtop10 = Movie.objects.order_by('-vote_average')[:10]
    # 내가 좋아하는 장르의 영화
    movies_gerne = Movie.objects.filter(genres__in=request.user.like_genres.all()).exclude(review__in=request.user.review_set.all()).order_by('-vote_average')[:10]
    # 내가 좋아하는 배우가 출연한 영화
    movies_cast = Movie.objects.filter(casts__in=request.user.like_casts.all()).exclude(review__in=request.user.review_set.all()).order_by('-vote_average')[:10]
    # 내가 좋아하는 감독이 연출한 영화
    movies = Movie.objects.filter(director__in=request.user.like_directors.all()).exclude(review__in=request.user.review_set.all()).order_by('-vote_average')[:10]



    context = {'movies': movies}
    return render(request, 'movies/main.html', context)

@login_required
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
        request.user.profile.point -= 100
        request.user.profile.save()
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
            request.user.profile.point += 10
            request.user.profile.save()
            data = {'userPk': comment.user.pk,
                    'username': comment.user.username,
                    'content': comment.content,
                    'moviePk' : movie_pk,
                    'reviewPk': review_pk,
                    'commentPk': comment.pk,
                    'count': review.comment_set.count()
                    }
            return JsonResponse(data)
    else:
        return HttpResponseBadRequest

@require_POST
@login_required
def delete_comment(request, comment_pk):
    if request.is_ajax():
        comment = get_object_or_404(Comment, pk=comment_pk)
        review = comment.review
        movie_pk = comment.review.movie.pk
        if request.user == comment.user or request.user.is_superuser:
            comment.delete()
            request.user.profile.point -= 10
            request.user.profile.save()
            data = {'count': review.comment_set.count(), 'reviewPk': review.pk}
            return JsonResponse(data)
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
                comment = form.save()
                if comment.like_users.filter(pk=request.user.id).exists():
                    is_like = "fas"
                else:
                    is_like = "far"
                data = {'userPk': comment.user.pk,
                        'username': comment.user.username,
                        'content': comment.content,
                        'moviePk' : comment.review.movie.pk,
                        'reviewPk': comment.review.pk,
                        'commentPk': comment.pk,
                        'commentLikes': comment.like_users.count(),
                        'isLike': is_like,
                        }
                return JsonResponse(data)
        else:
            messages.add_message(request, messages.WARNING, 'You are not a writer.')
            return redirect('movies:detail', movie_pk)
    else:
        return HttpResponseBadRequest

@login_required
@require_POST
def movie_like(request, movie_pk):
    if request.is_ajax():
        movie = get_object_or_404(Movie, pk=movie_pk)
        user = request.user
        if movie.like_users.filter(pk=user.id).exists():
            movie.like_users.remove(user)
            is_like = False
        else:
            movie.like_users.add(user)
            is_like = True
        return JsonResponse({'is_like': is_like, 'count': movie.like_users.count()})
    else:
        return HttpResponseBadRequest

@login_required
@require_POST
def cast_like(request, cast_pk):
    if request.is_ajax():
        cast = get_object_or_404(Cast, pk=cast_pk)
        user = request.user
        if cast.like_users.filter(pk=user.id).exists():
            cast.like_users.remove(user)
            is_like = False
        else:
            cast.like_users.add(user)
            is_like = True
        return JsonResponse({'is_like': is_like})
    else:
        return HttpResponseBadRequest

@login_required
@require_POST
def director_like(request, director_pk):
    if request.is_ajax():
        director = get_object_or_404(Director, pk=director_pk)
        user = request.user
        if director.like_users.filter(pk=user.id).exists():
            director.like_users.remove(user)
            is_like = False
        else:
            director.like_users.add(user)
            is_like = True
        return JsonResponse({'is_like': is_like})
    else:
        return HttpResponseBadRequest

@login_required
@require_POST
def review_like(request, review_pk):
    if request.is_ajax():
        review = get_object_or_404(Review, pk=review_pk)
        user = request.user
        if review.like_users.filter(pk=user.id).exists():
            review.like_users.remove(user)
            is_like = False
        else:
            review.like_users.add(user)
            is_like = True
        return JsonResponse({'is_like': is_like, 'count': review.like_users.count()})
    else:
        return HttpResponseBadRequest

@login_required
@require_POST
def comment_like(request, comment_pk):
    if request.is_ajax():
        comment = get_object_or_404(Comment, pk=comment_pk)
        user = request.user
        if comment.like_users.filter(pk=user.id).exists():
            comment.like_users.remove(user)
            is_like = False
        else:
            comment.like_users.add(user)
            is_like = True
        return JsonResponse({'is_like': is_like, 'count': comment.like_users.count()})
    else:
        return HttpResponseBadRequest