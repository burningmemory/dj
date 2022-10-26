from django.db import models
from django.utils import timezone
from django.urls import reverse


class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', default=timezone.now())

    def __str__(self):
        return str(self.author) + " \"" + str(self.name) + "\""
    
    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'pk': self.pk})