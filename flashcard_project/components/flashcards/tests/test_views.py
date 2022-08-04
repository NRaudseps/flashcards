# DJANGO
from django.test import TestCase
from django.test.client import Client
from django.urls import reverse

# THIS PROJECT
from flashcard_project.components.flashcards.models import FlashCard

# THIRDPARTY
from parameterized import parameterized


class ViewTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.flashcard = FlashCard.objects.create(
            question="My name is...", answer="Je m'appelle...", box=1
        )
        self.headers = {"HTTP_REFERER": "/"}

    @parameterized.expand(
        [
            ("index", None),
            ("new", None),
            ("edit", 1),
            ("box", 1),
        ]
    )
    def test_if_get_view_exists(self, url, data):
        """Test index page 200 status code response."""
        args = [data]
        if not data:
            args = []

        response = self.client.get(reverse(f"flashcards:{url}", args=args))
        self.assertEqual(response.status_code, 200)

    def test_index_page_returns_all_flashcards(self):
        """Test index page returns all flashcards."""
        response = self.client.get(reverse("flashcards:index"))
        self.assertEqual(
            list(response.context["flashcards"]), list(FlashCard.objects.all())
        )

    def test_create_flashcard_view(self):
        """Test create flashcard view."""
        data = {
            "question": "Hello",
            "answer": "Bonjour",
            "box": 1,
        }
        response = self.client.post(
            reverse("flashcards:create"), data=data, **self.headers
        )
        self.assertEqual(response.status_code, 302)
        self.assertIsNotNone(FlashCard.objects.get(question="Hello"))

    def test_update_flashcard_view(self):
        """Test update flashcard view"""
        data = {
            "question": "Hello",
            "answer": "Salut",
            "box": 1,
            "flashcard_pk": self.flashcard.id,
        }
        response = self.client.post(
            reverse("flashcards:update"), data=data, **self.headers
        )
        self.assertEqual(response.status_code, 302)

        self.flashcard.refresh_from_db()
        self.assertEqual(self.flashcard.answer, "Salut")

    def test_box_view_works_when_no_flashcards(self):
        """Test if box view works when no flashcards are in a box."""
        response = self.client.post(reverse("flashcards:box", args=[2]))
        self.assertEqual(response.status_code, 200)

    def test_flashcard_quiz_view_1(self):
        """Test flashcard quiz view when answer was correct."""
        data = {
            "flashcard_pk": self.flashcard.id,
            "answer": True,
        }

        response = self.client.post(reverse("flashcards:quiz"), data=data)
        self.assertEqual(response.status_code, 302)

        self.flashcard.refresh_from_db()
        self.assertEqual(self.flashcard.box, 2)

    def test_flashcard_quiz_view_2(self):
        """Test flashcard quiz view when answer wasn't correct."""
        self.flashcard.box = 2
        self.flashcard.save()
        data = {
            "flashcard_pk": self.flashcard.id,
            "answer": False,
        }

        response = self.client.post(reverse("flashcards:quiz"), data=data)
        self.assertEqual(response.status_code, 302)

        self.flashcard.refresh_from_db()
        self.assertEqual(self.flashcard.box, 1)
