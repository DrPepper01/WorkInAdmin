from django.db import models
from django.db.models import ForeignKey


class Author(models.Model):
    name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    date_of_birth = models.DateField()

    def __str__(self):
        return f'{self.name} {self.last_name} | {self.date_of_birth}'


class Book(models.Model):
    title = models.CharField(max_length=50)
    info = models.CharField(max_length=200)
    price = models.IntegerField()
    release_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.title} | {self.info} | {self.price}'

    class Meta:
        ordering = ('title', )


class Janre(models.Model):
    name = models.CharField(max_length=20)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)


