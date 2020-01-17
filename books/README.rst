=====
Books
=====

books is simple Django app which add, update, read and delete
books.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "books" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'books',
    ]

2. Include the books URLconf in your project urls.py like this::

    path('books/', include('books.urls')),

3. Run `python manage.py migrate` to create the books models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a books (you'll need the Admin app enabled).
   OR
   Visit http://127.0.0.1:8000/create

5. Visit http://127.0.0.1:8000/books/
