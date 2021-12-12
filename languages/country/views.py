from django.shortcuts import render
from rest_framework import generics
from .serializers import CountrySerialzer
from .models import Country

# CR views
class CountryList(generics.ListCreateAPIView):
    # queryset = Country.objects.filter(published = True)
    queryset = Country.objects.all()
    serializer_class = CountrySerialzer

# RUD view
class CountryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerialzer
