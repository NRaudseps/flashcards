# DJANGO
from django.test import TestCase

# THIS PROJECT
from flashcard_project.components.flashcards.models import FlashCard
from flashcard_project.components.flashcards.templatetags import project_tags


class TemplateTagTestCase(TestCase):
    def test_number_of_cards(self):
        for num in range(5):
            FlashCard.objects.create(question="Yes", answer="Oui", box=1)

        self.assertEqual(project_tags.number_of_cards(1), 5)

    def test_to_int(self):
        num = "5"
        self.assertEqual(project_tags.to_int(num), 5)
