from drf_spectacular.utils import extend_schema
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
# from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView

from .models import Book

from .serializers import BookSerializer

# class BookListAPIView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        books = Book.objects.all()
        serializer_data = BookSerializer(books, many=True).data
        data = {
            'response': f"Returen: {len(books)}",
            'books': serializer_data,
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
    # permission_classes = [AllowAny]
    def delete(self, requests, pk):
        book = Book.objects.get(pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class BookUpdateAPIView(generics.UpdateAPIView):
#     permission_classes = [AllowAny]
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

@extend_schema(
    request=BookSerializer,
    responses={
        'success': True,
        'message': 'Book created successfully',
        'data': BookSerializer,
    }
)
class BookUpdateAPIView(APIView):
    permission_classes = [AllowAny]
    def put(self, request, *args, **kwargs):
        book = get_object_or_404(Book, pk=kwargs['pk'])
        serializer = BookSerializer(instance=book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            response = {
                'success': True,
                'message': 'Book updated successfully',
                'data': serializer.data,
            }
            return Response(response, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class BookCreateAPIView(generics.CreateAPIView):
#     permission_classes = [AllowAny]
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

@extend_schema(
    request=BookSerializer,
    responses=BookSerializer
)
class BookCreateAPIView(APIView):
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([AllowAny])
def book_list(request, *args, **kwargs):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

# class BookRetrieveDeleteAPIView(generics.RetrieveDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookRetrieveDeleteAPIView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, *args, **kwargs):
        try:
            book = Book.objects.get(pk=kwargs['pk'])
            serializer = BookSerializer(book)
            return Response(serializer.data)
        except Book.DoesNotExist as e:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def delete(self, request, *args, **kwargs):
        try:
            book = Book.objects.get(pk=kwargs['pk'])
            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Book.DoesNotExist as e:
            return Response(status=status.HTTP_404_NOT_FOUND)