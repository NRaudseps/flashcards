# DJANGO
from django.http import HttpRequest
from django.shortcuts import HttpResponse, redirect, render
from django.views.decorators.http import require_http_methods

# THIS PROJECT
from flashcard_project.components.flashcards.forms import FlashCardForm
from flashcard_project.components.flashcards.models import Box, FlashCard


def index(request: HttpRequest) -> HttpResponse:
    """
    Main index page for flashcards.
    """
    form = FlashCardForm()
    context = {
        "flashcards": FlashCard.objects.all(),
        "boxes": Box.objects.all(),
        "form": form,
    }
    return render(request, template_name="index.html", context=context)


@require_http_methods(["POST"])
def create(request: HttpRequest) -> HttpResponse:
    """
    Create new flashcard object.
    """
    form = FlashCardForm(request.POST)
    if form.is_valid():
        form.save()

    return redirect("flashcards:index")
