from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def wszystkie(request):
    return HttpResponse("<h1>Tu będzie wyświetlana lista gier z bazy danych.</h1>")

