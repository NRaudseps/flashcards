# DJANGO
from django.http import HttpRequest
from django.shortcuts import HttpResponse, render


def index(request: HttpRequest) -> HttpResponse:
    """
    Main index page for flashcards.
    """
    return render(request, template_name="index.html")
