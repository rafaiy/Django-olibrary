from django import forms
from student.models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'cover', 'publisher', 'category')