from django.urls import path
from . import views
from .views import GenreListView, GenreCreateView, GenreRetrieveView, GenreUpdateView, GenreDestroyView
   
urlpatterns = [
    path('genre/', GenreListView.as_view(), name='genres'),
    path('genre/create', GenreCreateView.as_view(), name='genre_create' ),
    path('genre/<int:id>/', GenreRetrieveView.as_view(), name='genre'),
    path('genre/<int:id>/update/', GenreUpdateView.as_view(), name='genre_update'),
    path('genre/<int:id>/delete/', GenreDestroyView.as_view(), name='genre_delete'),
    path('movies/', views.MovieListCreateView.as_view(), name='movies'),
    path('movies/<int:id>/', views.MovieRetrieveUpdateDestroyView.as_view(), name='movie'),
]

