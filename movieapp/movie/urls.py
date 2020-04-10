from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('movies/', views.MovieList.as_view(),  name='movie-list'),
    path('movies/<int:pk>', views.MovieDetail.as_view(),  name='movie-detail'),
    path('users/', views.UserList.as_view(),  name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(),  name='user-detail'),
    path('', views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)
