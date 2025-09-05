from django.http import HttpResponse
from django.shortcuts import render
from .models import Book, BookInstance, Author
from django.views.generic import ListView, DetailView


def index(request):
    text_head = 'у нас большой выбор книг, у Читай-города меньше'
    books = Book.objects.all()
    num_books = Book.objects.all().count()
    num_instance = BookInstance.objects.all().count()
    num_instance_available =\
        BookInstance.objects.filter(status__exact=3).count()
    author = Author.objects
    num_author = Author.objects.count()
    context = {'text_head': text_head,
               'books': books, 'num_books':num_books,
               'num_instance': num_instance,
               'num_instance_available': num_instance_available,
               'author': author, 'num_author': num_author}
    return render(request, 'catalog/index.html', context)

class BookListView(ListView):
    model = Book
    paginate_by = 4
    context_object_name = 'books'

class BookDetailView(DetailView):
    model=Book
    context_object_name='book'


class AuthorListView(ListView):
    model = Author
    paginate_by = 4
    context_object_name = 'authors'

class AuthorDetailView(DetailView):
    model=Author
    context_object_name='author'



def about(request):
    return render(request, 'catalog/about.html')


def contacts(request):
    return render(request, 'catalog/contacts.html')