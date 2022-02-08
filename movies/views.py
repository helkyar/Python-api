# from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView

from .models import Genre
from .serializers import GenreSerializer
   
# GET views
class GenreListView(ListAPIView):
    serializer_class = GenreSerializer
    permission_classes = ()
    queryset = Genre.objects.all()

# POST views
class GenreCreateView(CreateAPIView):
    serializer_class = GenreSerializer
    permission_classes = ()