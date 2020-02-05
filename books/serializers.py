from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        # fields = ('id', 'name', 'price', 'description')
        exclude = ('is_online',)
