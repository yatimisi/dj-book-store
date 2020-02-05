from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters

from utils.permissions import IsAdminUserOrReadOnly

from .models import Book
from .serializers import BookSerializer, BookInfoSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ("is_online", "price")
    permission_classes = [IsAuthenticated, IsAdminUserOrReadOnly]

    def get_queryset(self):
        queryset = super().get_queryset()

        if not self.request.user.is_staff:
            return queryset.filter(is_online=True)

        return queryset

    def get_serializer_class(self):
        if not self.request.user.is_staff:
            return BookInfoSerializer

        return super().get_serializer_class()
