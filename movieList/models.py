from django.db import models
import datetime


# Create your models here.
class MovieBlock(models.Model):
    vote_count = models.PositiveIntegerField()
    movie_id = models.PositiveIntegerField()
    vote_average = models.DecimalField(
        max_digits=2, decimal_places=1, blank=True
    )
    title = models.CharField(max_length=500, blank=True)
    popularity = models.DecimalField(
        max_digits=7, decimal_places=3, default=0.000
    )
    poster_path = models.CharField(max_length=500, blank=True)
    backdrop_path = models.CharField(max_length=500, blank=True)
    original_language = models.CharField(max_length=5, blank=True)
    adult = models.BooleanField(
        default=False, help_text="check box if movie is for adults only"
    )
    overview = models.TextField(max_length=500, blank=True)
    release_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return (self.title)
