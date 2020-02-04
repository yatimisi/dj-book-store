from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .models import Book
from .serializers import BookSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.filter(is_online=True)
    serializer_class = BookSerializer
    permission_classes = []

    @action(['get'], False, 'all', 'all')
    def all_books(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
