from rest_framework import serializers
from .models import Artist, Genre, Album, Song


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:             #Meta class allows for defining of settings like serialized a model as well as fields to include or exclude in said serialization
        model = Artist
        fields = '__all__'
        
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'

class SongSerializer(serializers.ModelSerializer):
    genres = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = Song
        fields = '__all__'