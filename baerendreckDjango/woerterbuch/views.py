from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


def index(request):
    return render(request, 'woerterbuch/baerendreck.html')


def buchstabe(request):
    return render(request, 'woerterbuch/Wörtebuch.html')


def buchstabe_liste(request, pk):
    return render(request, 'woerterbuch/Buchstabe.html', {'buchstabe': get_object_or_404(Buchstabe, pk=buchstabe)})


def page_not_found(request):
    return render(request, 'woerterbuch/404.html')
