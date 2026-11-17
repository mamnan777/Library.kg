from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Book
from django.core.paginator import Paginator
from django.db.models import Q, F


def about_me(request):
    html = """
    <h1>Обо мне</h1>
    <p>привет миня завут пупупу</p>
    """
    return HttpResponse(html)

def my_favourite_writers(request):
    html = """
    <h1>Мои любимые писатели и поэты</h1>
    <p>1. Александр Сергеевич Пушкин</p>
    <p>2. Михаил Юрьевич Лермонтов</p>
    <p>3. Чингиз Торекулович Айтматов</p>
    """
    return HttpResponse(html)

def sayings_of_great_poets(request):
    html = """
    <h1>Высказывания великих поэтов</h1>
    <p>«Чтение — вот лучшее учение. Следовать за мыслями великого человека — есть наука самая занимательная.» — А. С. Пушкин</p>
    <img src="https://wikimedia.org" alt="А.С. Пушкин" width="250">
    """
    return HttpResponse(html)


def book_list_view(request):
    if request.method == 'GET':
        query = request.GET.get('q', '')
        books = Book.objects.all().order_by('-created_at')
        if query:
            books = books.filter(Q(titleicontains=query) | Q(authoricontains=query))
        paginator = Paginator(books, 5)
        page_obj = paginator.get_page(request.GET.get('page'))
        return render(request, 'book/book_list.html', {'page_obj': page_obj, 'query': query})


def book_detail_view(request, pk):
    if request.method == 'GET':
        book = get_object_or_404(Book, pk=pk)
        Book.objects.filter(pk=pk).update(views_count=F('views_count') + 1)
        book.refresh_from_db()
        return render(request, 'book/book_detail.html', {'book': book})