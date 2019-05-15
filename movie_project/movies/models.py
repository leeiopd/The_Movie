from django.db import models
from django.urls import reverse
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=20)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_genres', blank=True)
    def __str__(self):
        return f'Genre{self.pk}: {self.name}'
    
class Cast(models.Model):
    name = models.CharField(max_length=50)
    profile_path = models.TextField(blank=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_casts', blank=True)
    def __str__(self):
        return f'Cast{self.pk}: {self.name}'
    
class Director(models.Model):
    name = models.CharField(max_length=50)
    profile_path = models.TextField(blank=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_directors', blank=True)
    def __str__(self):
        return f'Director{self.pk}: {self.name}'
        
class Movie(models.Model):
    adult = models.BooleanField()
    original_language = models.CharField(max_length=20)
    original_title = models.TextField()
    overview = models.TextField(blank=True)
    release_date = models.CharField(max_length=30)
    revenue = models.IntegerField()
    runtime = models.IntegerField(blank=True)
    tagline = models.TextField(blank=True)
    title = models.TextField()
    vote_average = models.FloatField()
    genres = models.ManyToManyField(Genre, related_name='movies')
    casts = models.ManyToManyField(Cast, related_name='movies')
    role_data = models.TextField()
    poster_path = models.TextField()
    director = models.ForeignKey(Director, on_delete=models.PROTECT, blank=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies', blank=True)
    def __str__(self):
        return f'Movie{self.pk}: {self.title}'
        
class Review(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    score = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews', blank=True)
    def __str__(self):
        return f'Review{self.pk}: {self.title}'
    
class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_comments', blank=True)
    def __str__(self):
        return f'Comment{self.pk}: {self.content}'