from movieList.models import MovieBlock
from rest_framework import serializers


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MovieBlock
        fields = (
            'title',
            'movie_id',
            'video',
            'vote_average',
            'popularity',
            'vote_count',
            'vote_average',
            'poster_path',
            'backdrop_path',
            'overview',
            'original_language',
            'original_title',
            'adult',
            'genre_ids',
            'release_date'
        )
