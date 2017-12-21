from django.db import models
from django.shortcuts import reverse

class Category(models.Model):
    type = models.CharField(max_length=20)
    icon = models.CharField(max_length=500)
    def __str__(self):
        return self.type


class Book(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    cover = models.ImageField(upload_to='documents/')
    publisher = models.CharField(max_length=20)
    def __str__(self):
        return self.title+'-'+self.publisher

    def get_absolute_url(self):
        return reverse('index')
