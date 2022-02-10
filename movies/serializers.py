from rest_framework import serializers
from .models import Genre, Movie
   
class GenreSerializer(serializers.ModelSerializer):
    total_movies = serializers.SerializerMethodField()
       
    class Meta:
        model = Genre
        fields = ('id', 'name', 'total_movies')
        read_only_fields = ('id', )
   
        def get_total_movies(self, obj):
            return obj.movies.count()

class  MovieSerializer(serializers.ModelSerializer):
     
    class Meta:
        model = Movie
        fields = ('id', 'model', 'genre', 'release_date', )
        read_only_fields = ('id', )
        extra_kwargs = {
            'release_date': {'write_only': True},
        }
