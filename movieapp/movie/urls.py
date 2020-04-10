from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('movies/', views.MovieList.as_view()),
    path('movies/<int:pk>', views.MovieDetail.as_view()),
    path('users/', views.UserList.as_view()),  # new
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('', views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)
