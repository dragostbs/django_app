from django.shortcuts import render
from .models import Book
from .forms import BookForm


def main(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            books = Book(title=form.cleaned_data['title'],
                         author=form.cleaned_data['author'],
                         rating=form.cleaned_data['rating'],
                         published_countries=form.cleaned_data['published_countries'],
                         is_bestseller=form.cleaned_data['is_bestseller'])
            books.save()
            form = BookForm()
    else:
        form = BookForm()

    return render(request, 'data_app/main.html', {'form': form})
