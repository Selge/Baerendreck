from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


def index(request):
    return render(request, 'baerendreck.html')


def buchstabe(request):
    return render(request, 'Wörtebuch.html')


# def buchstabe_liste(request, pk):
#    return render(request, 'woerterbuch/../templates/Buchstabe.html', {'buchstabe': get_object_or_404(Buchstabe, pk=buchstabe)})


# def page_not_found(request):
#    return render(request, 'woerterbuch/../templates/404.html')
