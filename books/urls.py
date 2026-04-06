from django.urls import path

from .views import (BookListAPIView,
                    book_list,
                    BookDetailAPIView,
                    BookDeleteAPIView,
                    BookUpdateAPIView,
                    BookCreateAPIView,
                    BookRetrieveDeleteAPIView)

urlpatterns = [
    path('list/', BookListAPIView.as_view(), name='book-list'),
    path('book/<int:pk>/', BookDetailAPIView.as_view(), name='book-detail'),
    path('book/<int:pk>/delete/', BookDeleteAPIView.as_view(), name='book-delete'),
    path('book/<int:pk>/update/', BookUpdateAPIView.as_view(), name='book-update'),
    path('book/create/', BookCreateAPIView.as_view(), name='book-create'),
    path('list/func/', book_list, name='book-list'),
    path('book/retrieve-delete/<int:pk>/', BookRetrieveDeleteAPIView.as_view(), name='book-retrieve-delete'),
]