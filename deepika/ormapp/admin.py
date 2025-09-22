from django.contrib import admin
from .models import Movie_DB

class Movie_DBAdmin(admin.ModelAdmin):
    list_display = ('Movie_ID', 'Title', 'Genre', 'Rating', 'Language', 'Release_Date', 'Poster_URL')

admin.site.register(Movie_DB, Movie_DBAdmin)
