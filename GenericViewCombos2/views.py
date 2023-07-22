from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from GenericViewCombos2.models import Book2
from GenericViewCombos2.serializers import SerializersBook2


class BookListCreateAPIView2(ListCreateAPIView):
    queryset = Book2.objects.all()
    serializer_class = SerializersBook2


class BookRetrieveUpdateDestroy2(RetrieveUpdateDestroyAPIView):
    queryset = Book2.objects.all()
    serializer_class = SerializersBook2
    lookup_field = 'pk'