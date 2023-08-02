# DJANGO JAMMIN | MUSIC LIBRARY DB

## MoSCoW

<br>

## Must have
 1. Django framework
    - Django Rest Framework to build API routes for the CRUD operations.
    - Routes to perform CRUD operations for each model (Song, Album, Artist, etc.)

        - GET: Retrieve objects

        - POST: Create new objects

        - PUT/PATCH: Update existing objects

        - DELETE

 2. PostgreSQL DB to store music library data 

 3. Thunder Client to test API routes

 4. Relationship diagram to show relationships between models [Relationship Diagram](https://dbdiagram.io/d/64ca718c02bd1c4a5e2153ea)

 5. Models for each component such as Songs, albums, etc to represent data in DB

 6. Foreign key relationships as well as ManyToMany relationships between each model

 7. API routes to display info as JSON

## Should have
 1. Route to allow users to add a song to a playlist.

 2. Routes that accept query parameters (?query=search) to search/filter for data in models.

 3. Custom field to the API to keep track of the most popular songs based on playlist additions.

 4. Link up the database/API to a React frontend for a complete music library application.

## Could have
 1. Functionality for filtering a list of songs by artist or other criteria.

 2. User authentication and authorization to restrict access to certain API routes.


## Wont have
 1. Spotify's permission

<br>

## CRUD
READ - Serializers to read table info, songs, albums, artists, etc...

POST - Add new info/relationships in DB

UPDATE - Update existing DB info/relationships

DELETE - Get rid of DB info/relationships

<br>

## INIT
## USEFUL COMMANDS FOR DJANGO
- python -m pip install Django

- pip freeze > requirements.txt

- django-admin startproject (name)

- cd (name)

- python manage.py startapp (name)

- pip install djangorestframework

- python manage.py makemigrations

- python manage.py migrate

- python manage.py runserver

## Models.py
from django.db import models


class Artist(models.Model):

    name = models.CharField(max_length=100)


class Album(models.Model):

    label = models.CharField(max_length=200)


class Song(models.Model):

    title = models.CharField(max_length=200)

    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    genres = models.ManyToManyField(Genre)

<br>

## Urls.py

router = routers.DefaultRouter()

router.register(r'artists', views.ArtistViewSet)

router.register(r'albums', views.AlbumViewSet)

router.register(r'songs', views.SongViewSet)


urlpatterns = [

    path('api/', include(router.urls)),

]

<br>

## Views.py

class ArtistViewSet(viewsets.ModelViewSet):

    queryset = Artist.objects.all()

    serializer_class = ArtistSerializer


class AlbumViewSet(viewsets.ModelViewSet):

    queryset = Album.objects.all()

    serializer_class = AlbumSerializer


class SongViewSet(viewsets.ModelViewSet):

    queryset = Song.objects.all()

    serializer_class = SongSerializer

<br>

## ../settings.py

INSTALLED_APPS = [

    'rest_framework',

    'jams',

]

<br>

## API BUILD
<!-- Thank you claytonius -->

Django Rest Framework serializers. Stored as JSON for READing, but have the ability to fetch said data using urls.py


JSON output : {"song_id": 1, "song_name": Changes, "artist_id": 1, "artist_name": Black Sabbath, "album_id": 1, "album_label": Vol. 4}
