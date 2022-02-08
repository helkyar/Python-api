# from django.shortcuts import render

from .models import Genre
from .serializers import GenreSerializer
from rest_framework.generics import ListAPIView
   
class GenreListView(ListAPIView):
    serializer_class = GenreSerializer
    permission_classes = ()
    queryset = Genre.objects.all()
