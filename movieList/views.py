from .models import MovieBlock
from rest_framework import viewsets
from .serializers import MovieSerializer


class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows movies to be views or edited
    """
    queryset = MovieBlock.objects.all().order_by('title')
    serializer_class = MovieSerializer
