from django import forms
# from .models import Book


class BookForm(forms.Form):
    title = forms.CharField(label='Title', max_length=50)
    author = forms.CharField(label='Author', max_length=50)
    rating = forms.IntegerField(label='Rating', min_value=1, max_value=5)
    published_countries = forms.CharField(label='Published Countries', widget=forms.Textarea, max_length=200)
    is_bestseller = forms.BooleanField(label='Bestseller', required=False)


# class ReviewForm(forms.ModelForm):
#     class Meta:
#         model = Book
#         fields = '__all__'