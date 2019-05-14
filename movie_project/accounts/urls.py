from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('<int:user_id>/', views.userInfo, name='user_info'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('profile/update/info', views.updateProfile, name='updateProfile'),
    path('profile/update/genre', views.updateGenre, name='updateGenre'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.log_out, name='logout'),
    path('<int:user_id>/subscribe/', views.subscribe, name="subscribe"),
    path('profile/subscribes', views.mySubscribes, name='subscribes'),
    path('profile/subscribers', views.mySubscribers, name='subscribers'),

]