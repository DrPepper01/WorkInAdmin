from django.shortcuts import render
from .models import Book, Author
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
        return {'authors': Author.objects.all()}


class AuthorDetailView(DetailView):
    model = Author
    context_object_name = 'author'
    template_name = 'application/authors_detail.html'
    pk_url_kwarg = 'pk'

    # def get_context_data(self, **kwargs):
    #     context = super(AuthorDetailView, self).get_context_data(**kwargs)
    #     context['books'] = Book.objects.filter(author_id=book_id)
    #     return context



class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'application/book_detail.html'
