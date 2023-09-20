from django import forms
from .models import Book, Author


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = '__all__'
