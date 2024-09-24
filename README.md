# django-book-store

## Change Directory

~~~cmd
cd book_store
~~~

## Make Migrations

~~~cmd
python manage.py makemigrations
~~~

## Run Migrations

~~~cmd
python manage.py migrate
~~~

## Shell to insert entries in database

~~~cmd
python manage.py shell
~~~

## Inserting entries in database in shell

~~~python
from book_outlet.models import Book

harry_potter = Book(title="Harry Potter 1 - The Philosophers Stone",rating=5)

harry_potter.save()

lotr = Book(title="Lord of the Rings", rating=4)

lotr.save()
~~~

### Viewing object in shell

~~~python
from book_outlet.models import Book

Book.objects.all()
~~~

### Viewing particular attribute of Book object

~~~python
from book_outlet.models import Book

Book.objects.all()[0].title

Book.objects.all()[0].rating

Book.objects.all()[0].author

Book.objects.all()[0].is_bestselling
~~~

## Updating entries

~~~python
from book_outlet.models import Book

hp = Book.objects.all()[0]

lotr = Book.objects.all()[1]

hp.author = "J.K. Rowling"

hp.is_bestselling = True

hp.save()

lotr.author = "J.R.R. Tolkein"

lotr.is_bestselling = True

lotr.save()
~~~

### Deleting entries

~~~python
from book_outlet.models import Book

hp = Book.objects.all()[0]

hp.delete()

Book.objects.all()
~~~

## Inserting entries using create

~~~python
from book_outlet.models import Book

Book.objects.create(title="Harry Potter 1", rating=5, author="J.K. Rowling", is_bestselling=True)

Book.objects.create(title="My Book", rating=2, author="Utkarsh", is_bestselling=False)

Book.objects.create(title="Some Random Book", rating=1, author="Random", is_bestselling=False)  

Book.objects.all()
~~~

## Getting single datapoint with get

~~~python 
from book_outlet.models import Book

Book.objects.get(id=2)

Book.objects.get(title="My Book")

Book.objects.get(rating=5)
~~~

## Getting multiple datapoints with filter

~~~python 
from book_outlet.models import Book

Book.objects.filter(is_bestselling=True)

Book.objects.filter(is_bestselling=False, rating=2)

# Rating Lower than 3 
Book.objects.filter(rating__lt=3)

# Contains filter
Book.objects.filter(rating__lt=3, title__contains="Random")
~~~

## Or condition

~~~python 
from book_outlet.models import Book

from django.db.modles import Q

Book.objects.filter(Q(rating__lt=3) | Q(is_bestselling=True), Q(author__contains="Rowling"))
~~~

## Storing in variables

~~~python 
from book_outlet.models import Book

bestsellers = Book.objects.filter(is_bestselling=True)

amazing_bestsellers = Book.objects.filter(rating__gt=4, is_bestselling=True)

print(bestsellers)

print(amazing_bestsellers)
~~~

## Admin functionalities

### Create super user

~~~cmd
python manage.py createsuperuser
~~~

### Run server

~~~cmd
python manage.py runserver
~~~

### Accessing admin

Link - [http://localhost:8000/admin](http://localhost:8000/admin)