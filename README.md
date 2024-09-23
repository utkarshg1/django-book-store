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