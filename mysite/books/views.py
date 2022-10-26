from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Book
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


def index(request):
    question_list = Book.objects.order_by('-name')
    context = {
        'question_list': question_list,
    }
    return render(request, 'books/index.html', context)


def detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return HttpResponse(book)


class BookDetailView(DetailView):
    model = Book
    template_name = "books/book_detail.html"

class BookCreateView(CreateView):
    model = Book
    fields = ["name", "author"]

class BookUpdateView(UpdateView):
    model = Book
    fields = ["name", "author"]

class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy('index')