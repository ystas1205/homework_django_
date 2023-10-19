from django.shortcuts import render, reverse
from django.core.paginator import Paginator
from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    book_objects = Book.objects.order_by('pub_date')
    context = {'books': book_objects}
    return render(request, template, context)


def books_page(request, pub_date):
    template = 'books/book_pag.html'
    book_objects = Book.objects.filter(pub_date=pub_date)
    book_objects_lt = \
        Book.objects.filter(pub_date__lt=pub_date).order_by('pub_date').first()
    book_objects_gt = \
        Book.objects.filter(pub_date__gt=pub_date).order_by('pub_date').first()
    if book_objects_lt:
        book_lt = str(book_objects_lt.pub_date)
        print(book_lt)
    else:
        book_lt = None
    if book_objects_gt:
        book_gt = str(book_objects_gt.pub_date)
    else:
        book_gt = None
    context = {
        'books': book_objects,
        'page1': book_lt,
        'page2': book_gt,
    }
    return render(request, template, context)

