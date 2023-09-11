from django.contrib import admin
from application.models import Book, Author, Janre, Students, Courses

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Janre)
admin.site.register(Students)
admin.site.register(Courses)
