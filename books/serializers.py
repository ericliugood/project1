from rest_framework import serializers
from .models import Author,Book,BookAuthor,Store,Order,OrderRetail

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'created_at', 'updated_at']


class BookAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookAuthor
        fields = ['id', 'title','author','book','collaboration_year', 'created_at', 'updated_at']

class BookSerializer(serializers.ModelSerializer):
    authors = BookAuthorSerializer(many=True)  # 嵌套的 BookAuthor 序列化器
    
    class Meta:
        model = Book
        fields = ['id', 'title', 'created_at', 'updated_at']

    def create(self, validated_data):
        authors_data = validated_data.pop('authors')
        book = Book.objects.create(**validated_data)

        for author_data in authors_data:
            author_info = author_data.pop('author')
            author, created = Author.objects.get_or_create(**author_info)
            BookAuthor.objects.create(book=book, author=author, **author_data)

        return book

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