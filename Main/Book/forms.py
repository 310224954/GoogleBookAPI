from django import forms
from isbn_field import ISBNField
from django.shortcuts import get_object_or_404

from Book.models import Book, Author, BookCovers



class BookForm(forms.ModelForm):
    title = forms.CharField()
    publication_date = forms.CharField()
    authors = forms.ModelMultipleChoiceField(Author.objects.all())
    ISBN = ISBNField()
    pages = forms.IntegerField()
    language = forms.CharField()

    
    class Meta:
        model = Book
        fields = ["title", "publication_date", "authors", "ISBN", "pages", "language"]

class AuthorForm(forms.ModelForm):
    name = forms.CharField()
    
    class Meta:
        model = Author
        fields = ["name"]

    

class CoversForm(forms.ModelForm):    
    small_thumbnail = forms.CharField()
    big_thumbnail = forms.CharField()

    class Meta:
        model = BookCovers
        fields = ["small_thumbnail", "big_thumbnail"]