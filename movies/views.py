# from django.shortcuts import render
from rest_framework.generics import (CreateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView)

from rest_framework import generics
from rest_framework import filters as df

from rest_framework.permissions import IsAuthenticated

from .models import Genre, Movie
from .serializers import GenreSerializer, MovieSerializer
from .pagination import ResultsPagination
   
# GET views
class GenreListView(ListAPIView):
    serializer_class = GenreSerializer
    permission_classes = ()
    queryset = Genre.objects.all()
    # set pagination
    pagination_class = ResultsPagination
    # set filters
    filter_backends = (df.SearchFilter, df.OrderingFilter, )
    search_fields = ('name', )
    ordering_fields = ('name', )

# POST views
class GenreCreateView(CreateAPIView):
    serializer_class = GenreSerializer
    permission_classes = (IsAuthenticated, )

# GET specific movie
class GenreRetrieveView(RetrieveAPIView):
    serializer_class = GenreSerializer
    permission_classes = ()
    queryset = Genre.objects.all()
    lookup_field = 'id'

# UPDATE specific movie 
class GenreUpdateView(UpdateAPIView):
    serializer_class = GenreSerializer
    permission_classes = ()
    queryset = Genre.objects.all()
    lookup_field = 'id'

# DELETE 
class GenreDestroyView(DestroyAPIView):
    permission_classes = ()
    queryset = Genre.objects.all()
    lookup_field = 'id'

""" ================================================ """
""" ====== MULTIPLE SIMULTANEOUS OPERATIONS ======== """
""" ================================================ """
# GET-POST
class MovieListCreateView(generics.ListCreateAPIView):
    serializer_class = MovieSerializer
    permission_classes = ()
    queryset = Movie.objects.all()
    pagination_class = ResultsPagination
    filter_backends = (df.OrderingFilter, df.SearchFilter, )
# Change 'model' -----------------------------------------------------
    search_fields = ('model', )
    ordering_fields = ('model', )

# GET-PUT-DELETE
class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MovieSerializer
    permission_classes = ()
    queryset = Movie.objects.all()
    lookup_field = 'id'