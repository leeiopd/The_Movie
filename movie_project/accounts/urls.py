from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('<int:user_id>/', views.userInfo, name='user_info'),
    path('signup/', views.signup, name='signup'),
    path('update/profile/', views.updateUser, name='updateUser'),
    path('update/proflieTogenre', views.proflieTogenre, name='proflieTogenre'),
    path('update/genre/', views.updateGenre, name='updateGenre'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.log_out, name='logout'),
    path('<int:user_id>/subscribe/', views.subscribe, name="subscribe"),
    path('<int:user_id>/subscribeList/', views.subscribeList, name='subscribeList'),
    path('<int:user_id>/subscriberList/', views.subscriberList, name='subscriberList'),
    path('<int:user_id>/feed/', views.viewfeed, name='feed'),
    path('<int:user_id>/likes/casts/', views.likeCasts, name='likeCasts'),
    path('<int:user_id>/likes/directors/', views.likeDirectors, name='directors'),

    

]