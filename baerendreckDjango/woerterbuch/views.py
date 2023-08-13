from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'baerendreck.html')


def buchstabe(request):
    return render(request,)
