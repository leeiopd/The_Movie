from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('<int:user_id>/', views.userInfo, name='user_info'),
    path('signup/', views.signup, name='signup'),
    path('update/profile/', views.updateUser, name='updateUser'),
    path('update/proflieTogenre', views.proflieTogenre, name='proflieTogenre'),
    path('update/genre/', views.updateGenre, name='updateGenre'),
    path('login/', views.login, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('<int:user_id>/subscribe/', views.subscribe, name="subscribe"),
    path('<int:user_id>/subscribeList/', views.subscribeList, name='subscribeList'),
    path('<int:user_id>/subscriberList/', views.subscriberList, name='subscriberList'),
    path('<int:user_id>/feed/', views.viewfeed, name='feed'),
    path('<int:user_id>/favorites/casts/', views.favoritesCasts, name='favoritesCasts'),
    path('<int:user_id>/favorites/directors/', views.favoritesDirectors, name='favoritesDirectors'),
    path('<int:user_id>/favorites/genres/', views.favoritesGenres, name='favoritesGenres'),
    path('<int:user_id>/favorites/movies/', views.favoritesMovies, name='favoritesMovies'),
    path('<int:user_id>/reivewsList/', views.reviewsList, name='reviewsList'),
    path('rank/', views.rank, name='rank')
]