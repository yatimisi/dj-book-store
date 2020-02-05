from django.db import models
from django.contrib.auth import get_user_model

from books.models import Book


User = get_user_model()


class Order(models.Model):
    book = models.ForeignKey(Book, models.PROTECT)
    creator = models.ForeignKey(User, models.CASCADE)
    count = models.PositiveIntegerField()
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (
            ('book', 'creator', 'create_at'),
        )

    def __str__(self):
        return f'Order at {self.create_at}'
