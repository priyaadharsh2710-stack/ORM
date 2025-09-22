from django.db import models

class Movie_DB(models.Model):
    Movie_ID = models.CharField(max_length=20, primary_key=True)
    Title = models.CharField(max_length=100)
    Genre = models.CharField(max_length=20)
    Rating = models.IntegerField()
    Language = models.CharField(max_length=15)
    Release_Date = models.DateField()
    Poster_URL = models.URLField(max_length=200)

    def __str__(self):
        return self.Title
