from django.shortcuts import render
from . import models


def books_list(request):
    if request.method =='GET':
        books = models.Book.objects.all()
        return render(request, template_name='books.html',
                      context={'books':books})
