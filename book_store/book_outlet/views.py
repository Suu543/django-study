from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.db.models import Avg, Max, Min

from .models import Book
# Create your views here.


def index(request):
    # class ==> Dict ==> Django에서는 Key 값을 . 으로 표현 가능
    # title = Ascending
    # -title = Descending
    books = Book.objects.all().order_by("-title")     
    num_books = books.count()
    avg_rating = books.aggregate(Avg("rating")) # rating__avg, rating__min

    return render(request, "book_outlet/index.html", {
        "books": books,
        "total_number_of_books": num_books,
        "average_rating": avg_rating
    })


def book_detail(request, slug):
    # try:
    #     book = Book.objects.get(pk=id)
    # except:
    #     raise Http404()
    # book = get_object_or_404(Book, pk=id)

    book = get_object_or_404(Book, slug=slug)
    return render(request, "book_outlet/book_detail.html", {
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestseller": book.is_bestselling
    })
