from django.shortcuts import render
from .models import Book
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# Create your views here.


class AllView(TemplateView):
    template_name = 'application/index.html'
    context_object_name = 'books'

    def get_context_data(self, **kwargs):
        return {'books': Book.objects.all()}


class BookList(ListView):
    model = Book
    context_object_name = 'books'


class AuthorView(TemplateView):
    template_name = 'application/author_list.html'
    context_object_name = 'authors'

    def get_context_data(self, **kwargs):
        return {'authors': Book.objects.all()}
