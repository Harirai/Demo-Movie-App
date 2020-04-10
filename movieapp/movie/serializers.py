from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'release_date',
                  'director', 'language', 'rating', 'running_time', 'owner')


class UserSerializer(serializers.ModelSerializer):
    movies = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Movie.objects.all()
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'movies')
