# DJANGO
from django.test import TestCase
from django.test.client import Client
from django.urls import reverse

# THIS PROJECT
from flashcard_project.components.flashcards.models import Box, FlashCard


class ViewTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.url = reverse("flashcards:index")
        self.box = Box.objects.create(name="Box 1")
        self.flashcard = FlashCard.objects.create(
            question="My name is...", answer="Je m'appelle...", box=self.box
        )

    def test_index_page_response(self):
        """Test index page 200 status code response."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_index_page_returns_all_flashcards(self):
        """Test index page returns all flashcards."""
        response = self.client.get(self.url)
        self.assertEqual(
            list(response.context["flashcards"]), list(FlashCard.objects.all())
        )

    def test_create_flashcard_view(self):
        """Test create flashcard view."""
        data = {
            "question": "Hello",
            "answer": "Bonjour",
            "box": self.box,
        }
        response = self.client.post(reverse("flashcards:create"), data=data)
        self.assertEqual(response.status_code, 302)
