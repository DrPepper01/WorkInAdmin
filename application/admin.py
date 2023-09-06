from django.contrib import admin
from application.models import Book, Author, Janre

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Janre)
