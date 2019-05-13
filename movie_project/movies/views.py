from django.shortcuts import render, redirect
from django.db.models import Avg
from .models import Movie

# Create your views here.
def main(request):
    movies = Movie.objects.annotate(score_avg=Avg('review__score')).order_by('-score_avg')[:20]
    print(movies)
    return render(request, 'movies/main.html', {'movies': movies})