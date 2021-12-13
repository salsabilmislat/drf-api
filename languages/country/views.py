from django.shortcuts import render
from rest_framework import generics
from .serializers import CountrySerialzer
from .models import Country
from .permissions import IsAuthenticatedOrReadOnly

# CR views
class CountryList(generics.ListCreateAPIView):
    # queryset = Country.objects.filter(published = True)
    queryset = Country.objects.all()
    serializer_class = CountrySerialzer
    permission_classes = (IsAuthenticatedOrReadOnly,)

# RUD view
class CountryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerialzer
    permission_classes = (IsAuthenticatedOrReadOnly,)
