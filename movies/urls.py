from django.urls import path
from .views import GenreListView
   
urlpatterns = [
    path('genre/', GenreListView.as_view(), name='genre'),
]

