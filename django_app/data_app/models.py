from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# class Country(models.Model):
#     name = models.CharField(max_length=80)
#     code = models.CharField(max_length=2)


# class Address(models.Model):
#     street = models.CharField(max_length=80)
#     postal_code = models.CharField(max_length=7)
#     city = models.CharField(max_length=50)


# class Author(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)


# class Book(models.Model):
#     title = models.CharField(max_length=50)
#     rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
#     author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
#     is_bestseller = models.BooleanField(default=False)
#     published_countries = models.ManyToManyField(Country, null=False)


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.CharField(max_length=50, null=True)
    is_bestseller = models.BooleanField(default=False, null=True)
    published_countries = models.CharField(max_length=200, null=True)