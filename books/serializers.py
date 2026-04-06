from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'description', 'author','price', 'image', 'created_at', 'updated_at')

    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)
        book = Book.objects.filter(title=title, author=author).exists()
        if title.isdigit() or title.isnumeric():
            raise serializers.ValidationError('Book title is invalid')
        if book:
            raise serializers.ValidationError('Book already exists')
        return data