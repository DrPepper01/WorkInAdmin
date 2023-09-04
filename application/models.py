from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=50)
    info = models.CharField(max_length=200)
    price = models.IntegerField()
    release_date = models.DateField()

    def __str__(self):
        return f'{self.title} | {self.info} | {self.price}'

    class Meta:
        ordering = ('title', )

