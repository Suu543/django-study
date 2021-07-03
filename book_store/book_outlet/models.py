from django.core import validators
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Countries" 


class Address(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(
        Address, on_delete=models.CASCADE, null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    # book_set
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, null=True, related_name="books")
#    author = models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default=False)
    # harry potter ==> harry-potter-1
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)
    published_countries = models.ManyToManyField(Country, related_name="books")

    def get_absolute_url(self):
        # return reverse("book-detail", args=[self.id])
        return reverse("book-detail", args=[self.slug])

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.rating})"

# python manage.py makemigrations
# python manage.py migrate

# from book_outlet.models import Book
# Book.objects.all()
# Book.objects.all()
# Book.objects.all()[1].author
# Book.objects.all()[1].is_bestselling

# Update Data
# harry_potter = Book.objects.all()
# harry_potter = Book.objects.all()[0]
# harry_potter.title
# lotr = Book.objects.all()[1]
# lotr.title

# harry_potter.author = 'J.K Rowling'
# harry_potter.is_bestselling = True
# harry_potter.save()

# lotr.author = 'J.R.R Tolkein'
# lotr.is_bestselling = True
# lotr.save()

# Book.objects.all()[0].author
# Book.objects.all()[1].author

# Delete Data
# harry_potter = Book.objects.all()[0]
# harry_potter.delete()
# Book.objects.all()

# Create Instead of Save
# Book.objects.create(title="Some random", rating=5, author="J.K Rowling", is_bestselling=True)
# Book.objects.create(title="Some random", rating=5, author="J.K Rowling", is_bestselling=True)

# Querying and Filtering Data
# Book.objects.get(id=3)
# Book.objects.get(id=2)
# Book.objects.get(title="My Story")

# Multiple Data
# Book.objects.filter(is_bestselling=True)
# Book.objects.filter(is_bestselling=True, rating=2)
# __lte or __lt
# Book.objects.filter(rating__lt=3)

# __contains ==> Case Sensitive
# __icontains ==> Case Insensitive
# Book.objects.filter(rating__lt=3, title__contains="Story")

# or Conditions
# from django.db.models import Q
# | = or , = and
# Books.objects.filter(Q(rating__lt = 3) | Q(is_bestselling=True), Q(author="J.K. Rowling"))
# 마지막 Q는 생략가능
# Books.objects.filter(Q(rating__lt = 3) | Q(is_bestselling=True), author="J.K. Rowling")

# Query Performance
# Book(title="...").save()
# bestsellers = Book.objects.filter(is_bestselling=True)
# 아직 DB에 접근한 상태는 아님
# bestsellers 변수를 가지고 어떤 행위를 해야 DB에 접근함
# amazing_bestsellers = bestsellers.filter(rating__gt=4)
# 이 시점에 실제로 DB에 접근해 Caching 함
# print(bestsellers)
# print(Book.objects.filter(rating__gt=3))
# good_books = Book.objects.filter(rating__gt=3)
# print(good_books)

# You can get multiple model instances (GET)
# You can delete multiple model instances
# You can update multiple model instances
# You can create multiple model instances

# Preparing Templates

# Adding a SlugField & Overwriting Save
# Book.objects.get(title="Harry Potter 1").save()
# Book.objects.get(title="Harry Potter 1").slug
# Book.objects.get(title="My Story").save()
# Book.objcets.get(title="My Story").slug

# Using the Slug & Updating Field Options

# Aggregation & Ordering

# One-to-one Python Code
# >> > from book_outlet.models import Author, Address, Book
# >> > Author.objects.all()
# <QuerySet [< Author: J.K. Rowling > ] >
# >> > Author.objects.all()[0].address
# >> > addr1 = Address(street="Some Street", postal_code="12345", city="London")
# >> > addr2 = Address(street="Another Street", postal_code="67890", city="New York")
# >> > addr1.save()
# >> > addr2.save()
# >> > jkr = Author.objects.get(first_name="J.K.")
# >> > jkr.address
# >> > jkr.address = addr1
# >> > jkr.save()
# >> > new_author = Author(address=addr1)
# >> > jkr.address
# <Address: Address object(1) >
# >> > jkr.address.street
# 'Some Street'
# >> > Address.objects.all()
# <QuerySet [ < Address: Address object (1) > , < Address: Address object (2) > ] >
# >> > Address.objects.all()[0].author
# <Author: J.K. Rowling >
# >> > Address.objects.all()[0].author.first_name
# 'J.K.'


# from book_outlet.models import Country, Book
# Book.objects.all()
# hp1 = Book.objects.all()[0]
# hp1.published_countries
# hp1.published_countries.all()

# germany = Country(name="Germany", code="DE")
# Book.objects.all()
# mys = Book.objects.all()[1]
# mys.published_countries.add(german)
# mys.published_countries.add(korea)
# mys.published_countries.all()
# mys.published_countries.all()[0]

# lon = Country.objects.all()[0]
# lon.books.all()
