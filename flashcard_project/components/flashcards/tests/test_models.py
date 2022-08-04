# DJANGO
from django.test import TestCase

# THIS PROJECT
from flashcard_project.components.flashcards.models import FlashCard


class FlashCardModelTestCase(TestCase):
    def test_move_1(self):
        card = FlashCard.objects.create(question="Hello", answer="Salut", box=1)
        card.move(solved=True)

        self.assertEqual(card.box, 2)

    def test_move_2(self):
        card = FlashCard.objects.create(question="Hello", answer="Salut", box=3)
        card.move(solved=False)

        self.assertEqual(card.box, 1)
