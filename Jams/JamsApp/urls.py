from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'genres', views.GenreViewSet)
router.register(r'artists', views.ArtistViewSet)
router.register(r'songs', views.SongViewSet)
router.register(r'albums', views.AlbumViewSet)

urlpatterns = [
    path('', include(router.urls)),
]