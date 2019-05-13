from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('<int:user_id>/', views.userInfo, name='info'),
    path('signup/', views.signup, name='signup'),
    path('update/', views.update, name='update'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.log_out, name='logout'),

]