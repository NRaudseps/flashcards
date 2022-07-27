# DJANGO
from django.test import TestCase

# THIS PROJECT
from flashcard_project.components.flashcards import models


class ModelTestCase(TestCase):
    def setUp(self) -> None:
        self.box = models.Box.objects.create(name="Box 1")

    def test_box_str(self):
        """Test box model __str__ method"""
        self.assertEqual(self.box.__str__(), "Box 1")
