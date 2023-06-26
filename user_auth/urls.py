from django.urls import path, include, re_path
from . import views

app_name = 'user_auth'
urlpatterns = [
path('', views.user_login, name='login'),
path('authenticate_user/', views.authenticate_user, name='authenticate_user'),
path('logout/', views.logout_user, name='logout'),
path('register/', views.create_user, name='register'),
]
