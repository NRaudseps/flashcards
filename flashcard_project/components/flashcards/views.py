# DJANGO
from django.http import HttpRequest
from django.shortcuts import HttpResponse, get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods

# THIS PROJECT
from flashcard_project.components.flashcards.forms import FlashCardForm
from flashcard_project.components.flashcards.models import Box, FlashCard


def index(request: HttpRequest) -> HttpResponse:
    """
    Main index page for flashcards.
    """
    context = {
        "flashcards": FlashCard.objects.all(),
        "boxes": Box.objects.all(),
    }
    return render(request, template_name="index.html", context=context)


def new(request: HttpRequest) -> HttpResponse:
    """
    Page for creating new flashcards.
    """
    form = FlashCardForm()
    context = {"form": form}
    return render(request, template_name="new.html", context=context)


@require_http_methods(["POST"])
def create(request: HttpRequest) -> HttpResponse:
    """
    Create new flashcard object.
    """
    form = FlashCardForm(request.POST)
    if form.is_valid():
        form.save()

    return redirect("flashcards:index")


def edit(request: HttpRequest, pk: int) -> HttpResponse:
    """
    Page for editing flashcards.
    """
    flashcard = get_object_or_404(FlashCard, pk=pk)
    form = FlashCardForm(instance=flashcard)
    context = {"form": form, "pk": pk}
    return render(request, template_name="edit.html", context=context)


@require_http_methods(["POST"])
def update(request: HttpRequest) -> HttpResponse:
    """
    Update existing flashcard.
    """
    flashcard = get_object_or_404(FlashCard, pk=request.POST["flashcard_pk"])

    form = FlashCardForm(request.POST, instance=flashcard)
    if form.is_valid():
        form.save()

    return redirect("flashcards:index")
