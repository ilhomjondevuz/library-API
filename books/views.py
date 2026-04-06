from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book

from .serializers import BookSerializer

# class BookListAPIView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookListAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        data = {
            'response': f"Returen: {len(books)}",
            'books': serializer.data,
            'status': status.HTTP_200_OK,
        }
        return Response(data)

class BookDetailAPIView(generics.RetrieveDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# class BookDeleteAPIView(generics.DestroyAPIView):
#     permission_classes = [AllowAny]
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookDeleteAPIView(APIView):
    permission_classes = [AllowAny]
    def delete(self, requests, pk):
        book = Book.objects.get(pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BookUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [AllowAny]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookCreateAPIView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = Book.objects.all()
    serializer_class = BookSerializer


@api_view(['GET'])
@permission_classes([AllowAny])
def book_list(request, *args, **kwargs):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

class BookRetrieveDeleteAPIView(generics.RetrieveDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer