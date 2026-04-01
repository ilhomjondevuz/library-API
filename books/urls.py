from django.urls import path

from .views import BookListAPIView

urlpatterns = [
    path('list/', BookListAPIView.as_view(), name='book-list'),
]