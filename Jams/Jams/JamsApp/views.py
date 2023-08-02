from django.shortcuts import render
from rest_framework import viewsets
from .models import Artist, Genre, Album, Song
from .serializers import ArtistSerializer, GenreSerializer, AlbumSerializer, SongSerializer
