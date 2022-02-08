from django.urls import path
from .views import GenreListView, GenreCreateView
   
urlpatterns = [
    path('genre/', GenreListView.as_view(), name='genre'),
    path('genre/create', GenreCreateView.as_view(), name='genre_create' )
]

