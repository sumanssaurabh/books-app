from django.db import models
from django.forms import ModelForm, TextInput
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError

# Create your models here.
class Book(models.Model):
    bookName = models.CharField(_("Book Name"), max_length=50, unique=True)
    bookPages = models.CharField(_("Book Pages"), max_length=50)
    bookPrice = models.CharField(_("Book Price"), max_length=50)

    def __str__(self):
        return self.bookName


class bookForm(ModelForm):
    def clean_bookname(self):
        bookname = self.cleaned_data["bookName"]
        if Book.objects.filter(bookName=bookname).exists():
            raise ValidationError("BookName already exists")
        return bookname

    class Meta:
        model = Book
        fields = "__all__"

        widgets = {
            "bookName": TextInput(attrs={"placeholder": "bookName"}),
            "bookPages": TextInput(attrs={"placeholder": "bookPages"}),
            "bookPrice": TextInput(attrs={"placeholder": "bookPrice"}),
        }
