from django.contrib import admin
from student.models import Book, Category

admin.site.register(model_or_iterable=Book)
admin.site.register(model_or_iterable=Category)