from django.shortcuts import render
from .models import Book, Author
from .forms import BookForm
from django.views.generic import TemplateView, FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

# Create your views here.


class AllView(TemplateView):
    template_name = 'application/index.html'
    context_object_name = 'books'

    # def get_context_data(self, **kwargs):
    #     return {'books': Book.objects.all()}
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book_list = Book.objects.all()
        paginator = Paginator(book_list, 3)  # Разбить на страницы по 10 книг на каждой странице
        page = self.request.GET.get('page')
        books = paginator.get_page(page)
        context['books'] = books
        return context


class BookList(ListView):
    paginate_by = 2
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author = self.get_object()
        books = author.bookies.all()
        context['courses'] = author.courses.all()
        context['books'] = books
        return context


class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'application/book_detail.html'


class AddBookView(LoginRequiredMixin, CreateView):
    model = Book
    fields = '__all__'
    success_url = '/books/'
    template_name = 'application/form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_name'] = 'Создание Книги'
        return context


class UpdateBookView(LoginRequiredMixin, UpdateView):
    model = Book
    fields = '__all__'
    success_url = '/books/{id}'
    template_name = 'application/form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_name'] = 'Обновить Книгу'
        context['update_text'] = True
        context['action'] = 'Обновить'
        return context


class DeleteBookView(LoginRequiredMixin, DeleteView):
    model = Book
    fields = '__all__'
    success_url = '/books/'
    template_name = 'application/form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_name'] = 'Удалить Книгу'
        context['update_text'] = True
        context['action'] = 'Удалить'
        return context



