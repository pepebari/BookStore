from Books.models import User, Genre, Stock, Book, Purchase
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'birth_date', 'register_date', 'phone_number', 'points']


class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genre
        fields = ['name']


class StockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stock
        fields = ['quantity']


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'genre', 'quantity', 'price', 'register_date']


class PurchaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Purchase
        fields = ['user', 'book']
