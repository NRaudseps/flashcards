# DJANGO
from django import template

from ..models import FlashCard

register = template.Library()


@register.simple_tag
def number_of_cards(box_number):
    """
    Return number of flashcards in a box.
    """
    return len(FlashCard.objects.filter(box=box_number))


@register.filter
def to_int(value):
    """
    Return value as an integer.
    """
    return int(value)
