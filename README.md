# Ex02 Django ORM Web Application
## Date: 18/09/2025

## AIM
To develop a Django application to store and retrieve data from a Movies Database using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```

admin.py

from django.contrib import admin
from .models import Movie_DB

class Movie_DBAdmin(admin.ModelAdmin):
    list_display = ('Movie_ID', 'Title', 'Genre', 'Rating', 'Language', 'Release_Date', 'Poster_URL')

admin.site.register(Movie_DB, Movie_DBAdmin)

models.py

from django.db import models

class Movie_DB(models.Model):
    Movie_ID = models.CharField(max_length=20, primary_key=True)
    Title = models.CharField(max_length=100)
    Genre = models.CharField(max_length=20)
    Rating = models.IntegerField()
    Language = models.CharField(max_length=15)
    Release_Date = models.DateField()
    Poster_URL = models.URLField(max_length=200)

    def _str_(self):
        return self.Title
```

## OUTPUT

![Uploading WhatsApp Image 2025-10-07 at 20.32.30_70244aae.jpg…]()



## RESULT
Thus the program for creating movies database using ORM hass been executed successfully
