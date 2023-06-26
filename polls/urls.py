from django.urls import path, include, re_path
from . import views

app_name = 'polls'
urlpatterns = [
path('', views.index, name='index'),
path('poll/', views.poll, name='poll'),
path('<int:question_id>', views.detail, name='detail'),
path('<int:question_id>/results/', views.results, name='results'),
path('<int:question_id>/vote/', views.vote, name='vote'),
re_path(r'^blog/(?P<year>[0-9]{4})/$',views.results)

]

