from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from GenericViewCombos1.models import Book1
from GenericViewCombos1.serializers import SerializersBook1



class BookListCreateAPIView(ListCreateAPIView):
    queryset = Book1.objects.all()
    serializer_class = SerializersBook1


class BookRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Book1.objects.all()
    serializer_class = SerializersBook1
    lookup_field = 'pk'