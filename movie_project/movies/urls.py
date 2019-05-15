from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.main, name='main'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('<int:movie_pk>/create/', views.create, name='create'),
    path('<int:movie_pk>/<int:review_pk>/delete/', views.delete, name='delete'),
    path('<int:movie_pk>/<int:review_pk>/update/', views.update, name='update'),
    # path('<int:movie_pk>/<int:review_pk>/detail/', views.review_detail, name='review_detail'),
    path('<int:movie_pk>/<int:review_pk>/create/', views.create_comment, name='create_comment'),
    path('<int:comment_pk>/delete/', views.delete_comment, name='delete_comment'),
    path('<int:comment_pk>/update/', views.update_comment, name='update_comment'),
    path('<int:movie_pk>/movie_like/', views.movie_like, name='movie_like'),
    path('<int:director_pk>/director_like/', views.director_like, name='director_like'),
    path('<int:cast_pk>/cast_like/', views.cast_like, name='cast_like'),
]