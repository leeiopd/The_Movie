from django.contrib import admin
from .models import Genre, Cast, Director, Movie, Review, Comment

# Register your models here.
class GenreAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')

class CastAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')

class MovieAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'content')

admin.site.register(Genre, GenreAdmin)
admin.site.register(Cast, CastAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)