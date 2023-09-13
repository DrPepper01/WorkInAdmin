"""
URL configuration for Books2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from application.views import AllView, BookList, AuthorView, AuthorDetailView, BookDetailView, AddBookView, \
    UpdateBookView, DeleteBookView


urlpatterns = [

    path('admin/', admin.site.urls),
    path('', AllView.as_view(), name='main_page'),
    path('authors/', AuthorView.as_view(), name='author_list'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='authors_detail'),
    path('books/', BookList.as_view(), name='books_list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='books_detail'),
    path('books/add/', AddBookView.as_view(), name='add_book'),
    path('books/<int:pk>/update', UpdateBookView.as_view(), name='upd_book'),
    path('books/<int:pk>/delete', DeleteBookView.as_view(), name='delete_book'),



]
