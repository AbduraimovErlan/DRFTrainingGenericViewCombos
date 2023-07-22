from rest_framework import serializers
from GenericViewCombos2.models import Book2



class SerializersBook2(serializers.ModelSerializer):
    class Meta:
        model = Book2
        fields = '__all__'