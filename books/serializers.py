from rest_framework import serializers
from .models import Author,Book,BookAuthor,Store,Order,OrderRetail

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'created_at', 'updated_at']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'created_at', 'updated_at']


class BookAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookAuthor
        fields = ['id', 'title','author','book','collaboration_year', 'created_at', 'updated_at']


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['id', 'name', 'created_at', 'updated_at']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'store', 'created_at', 'updated_at']


class OrderRetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderRetail
        fields = ['id', 'order','book','quantity', 'created_at', 'updated_at']