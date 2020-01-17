from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Book, bookForm

# from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


def cheat(request):
    return render(request, "books/cheat.html")


def test(request):
    if request.method == "POST":
        bookName = request.POST["id"]
        book = Book.objects.get(id=bookName)
        frm = bookForm(request.POST, instance=book)
        if frm.is_valid():
            print("cleaned data:", frm.cleaned_data)
            frm.save()

    forms = []
    books = Book.objects.all()
    context = {"books": books}
    for book in books:
        form = bookForm(instance=book)
        # print(form)
        forms.append(form)
    # context = {"forms": forms, "sucess": "Book Updated Sucessfully"}
    context = {"forms": forms, "books": books, "sucess": "Book Updated Sucessfully"}
    return render(request, "books/test.html", context)


def index(request):
    return render(request, "books/index.html")


def create(request):
    form = bookForm(request.POST or None)
    context = {"form": form}
    if form.is_valid():
        print(form.cleaned_data)
        form.save()
        form = bookForm()
        context = {"form": form, "sucess": "Book Created Sucessfully"}

    return render(request, "books/create.html", context)


def read(request):
    books = Book.objects.all()
    return render(request, "books/view.html", {"books": books})


def update(request):
    if request.method == "POST":
        print(request.POST)
        id = request.POST["id"]
        # book = Book.objects.get(bookName=bookName)
        try:
            # book = get_object_or_404(Book, bookName=bookName)
            # obj = get_object_or_404(MyModel, pk=1)
            book = Book.objects.get(id=id)
            frm = bookForm(request.POST or None, instance=book)
        except Book.DoesNotExist:
            frm = bookForm(request.POST or None)

        print(frm)
        if frm.is_valid():
            print("cleaned data:", frm.cleaned_data)
            frm.save()
    forms = []
    books = Book.objects.all()
    for book in books:
        form = bookForm(instance=book)
        # print(form)
        forms.append(form)
    context = {"forms": forms, "sucess": "Book Updated Sucessfully"}
    return render(request, "books/update.html", context)


def edit(request, book_id):
    try:
        # book = get_object_or_404(Book, bookName=bookName)
        # obj = get_object_or_404(MyModel, pk=1)
        book = Book.objects.get(id=book_id)
        frm = bookForm(request.POST or None, instance=book)
    except Book.DoesNotExist:
        frm = bookForm()

    print(frm)
    if frm.is_valid():
        print("cleaned data:", frm.cleaned_data)
        frm.save()
    return render(request, "books/edit.html", {"form": frm})


def delete(request):
    books = Book.objects.all()
    context = {"books": books}
    if request.method == "POST":
        id = request.POST["id"]
        print(id)
        book = Book.objects.get(id=id)
        book.delete()
        # form.save()
        # form = bookForm()
        context = {"books": books, "sucess": "Book Deleted Sucessfully"}
    return render(request, "books/delete.html", context)


def crud(request):
    print(request.POST)
    if request.method == "POST":
        if request.POST.get("action") == "add":
            # add
            form = bookForm(request.POST or None)
            # context = {"form": form}
            if form.is_valid():
                print(form.cleaned_data)
                form.save()
                # form = bookForm()
                # context = {"form": form, "sucess": "Book Created Sucessfully"}

        if request.POST.get("action") == "save":
            # update
            id = request.POST["id"]
            try:
                book = Book.objects.get(id=id)
                frm = bookForm(request.POST, instance=book)
            except Book.DoesNotExist:
                frm = bookForm(request.POST)

            # print(frm)
            if frm.is_valid():
                print("cleaned data:", frm.cleaned_data)
                frm.save()
            pass
        if request.POST.get("action") == "delete":
            # delete
            pass
            id = request.POST["id"]
            print(id)
            book = Book.objects.get(id=id)
            book.delete()
    # read
    forms = []
    books = Book.objects.all()
    for book in books:
        form = bookForm(instance=book)
        # print(form)
        forms.append(form)
    # context = {"forms": forms, "sucess": "Book Updated Sucessfully"}
    form = bookForm()
    context = {"forms": forms, "form": form, "sucess": "Book Updated Sucessfully"}

    return render(request, "books/crud.html", context)

