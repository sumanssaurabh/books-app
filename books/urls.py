from django.urls import path

from .views import index, create, read, delete, update, crud, edit, test, cheat

app_name = "books"

urlpatterns = [
    path("", index, name="index"),
    path("create/", create, name="create"),
    path("read/", read, name="read"),
    path("update/", update, name="update"),
    path("delete/", delete, name="delete"),
    path("edit/<int:book_id>", edit, name="crud"),
    path("crud/", crud, name="crud"),
    path("test/", test, name="test"),
    path("cheat/", cheat, name="cheat"),
]

