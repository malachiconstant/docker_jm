from django.contrib import admin
from .models import MovieBlock


# Register your models here.
@admin.register(MovieBlock)
class MovieBlockAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'movie_id', 'video', 'genre_ids')
        }),
        (None, {
            'fields': ('popularity', 'vote_count', 'vote_average')
        }),
        ('Images', {
            'fields': ('poster_path', 'backdrop_path')
        }),
        (None, {
            'fields': (
                'overview', 'original_language',
                'original_title', 'adult', 'release_date'
            )
        })
    )
    list_display = ('title', 'release_date', 'movie_id')
    save_on_top = True
