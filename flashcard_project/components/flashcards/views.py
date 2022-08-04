# DJANGO
from django.http import HttpRequest
from django.shortcuts import (
    HttpResponse,
    get_list_or_404,
    get_object_or_404,
    redirect,
    render,
)
from django.urls import reverse
from django.views.decorators.http import require_http_methods

# THIS PROJECT
from flashcard_project.components.flashcards.forms import FlashCardForm
from flashcard_project.components.flashcards.models import FlashCard


def index(request: HttpRequest) -> HttpResponse:
    """
    Main index page for flashcards.
    """
    context = {"flashcards": FlashCard.objects.all()}
    return render(request, template_name="pages/index.html", context=context)


def new(request: HttpRequest) -> HttpResponse:
    """
    Page for creating new flashcards.
    """
    form = FlashCardForm()
    context = {"form": form}
    return render(request, template_name="pages/new.html", context=context)


@require_http_methods(["POST"])
def create(request: HttpRequest) -> HttpResponse:
    """
    Create new flashcard object.
    """
    form = FlashCardForm(request.POST)
    if form.is_valid():
        form.save()

    return redirect(request.META.get("HTTP_REFERER"))


def edit(request: HttpRequest, pk: int) -> HttpResponse:
    """
    Page for editing flashcards.
    """
    flashcard = get_object_or_404(FlashCard, pk=pk)
    form = FlashCardForm(instance=flashcard)
    context = {"form": form, "pk": pk}
    return render(request, template_name="pages/edit.html", context=context)


@require_http_methods(["POST"])
def update(request: HttpRequest) -> HttpResponse:
    """
    Update existing flashcard.
    """
    flashcard = get_object_or_404(FlashCard, pk=request.POST["flashcard_pk"])

    form = FlashCardForm(request.POST, instance=flashcard)
    if form.is_valid():
        form.save()

    return redirect(request.META.get("HTTP_REFERER"))


def box(request: HttpRequest, pk: int) -> HttpResponse:
    """
    Page for viewing flashcards in a box.
    """
    flashcards = get_list_or_404(FlashCard, box=pk)

    context = {"flashcards": flashcards, "box_num": pk}
    return render(request, template_name="pages/box.html", context=context)


@require_http_methods(["POST"])
def quiz(request: HttpRequest) -> HttpResponse:
    """
    Move flashcards to other boxes when user answers.
    """
    answer = request.POST["answer"]
    flashcard = get_object_or_404(FlashCard, pk=request.POST["flashcard_pk"])
    original_box_number = flashcard.box
    flashcard.move(solved=True) if answer == "True" else flashcard.move(solved=False)

    return redirect(reverse("flashcards:box", args=[original_box_number]))
