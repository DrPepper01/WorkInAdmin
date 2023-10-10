from django import forms
from .models import Book, Author


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class AddAuthorForm(forms.ModelForm):

    name = forms.CharField(label='Имя автора')
    last_name = forms.CharField(label='Фамилия автора')
    date_of_birth = forms.DateField()

    class Meta:
        model = Author
        fields = '__all__'
