from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('bootstrap/', views.bootstrap, name='bootstrap'),
    path('inndexx/', views.inndexx, name='inndexx')
]

