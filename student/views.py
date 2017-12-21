from django.shortcuts import render
from django.views.generic import ListView, View, CreateView
from student.models import Category, Book
from student.forms import BookForm
from django.shortcuts import redirect

def model_form_upload(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BookForm()
    return render(request, 'student/model_form_upload.html', {
        'form': form
    })

def IndexView(request):
    all = Category.objects.all()
    return render(request, template_name='student/index.html', context={'allcategory': all})

def Cat(request, id):
    books = Category.objects.get(pk=id).book_set.all()
    return render(request, template_name='student/cat.html', context={'books': books})

class AddBook(CreateView):
    model = Book
    fields = ['category', 'title', 'author', 'cover', 'publisher']
