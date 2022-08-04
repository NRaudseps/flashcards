# DJANGO
from django.db import models


class FlashCard(models.Model):
    MAX_BOX_COUNT = 5
    BOXES = range(1, MAX_BOX_COUNT + 1)

    class Meta:
        app_label = "flashcards"

    question = models.CharField(max_length=1028)
    answer = models.CharField(max_length=1028)
    box = models.IntegerField(default=BOXES[0], choices=zip(BOXES, BOXES))
    pub_date = models.DateTimeField(auto_now_add=True)

    def move(self, solved: bool) -> None:
        """
        Move flashcard to other boxes when user does a quiz.
        """
        next_box = self.box + 1 if solved else self.BOXES[0]

        if next_box in self.BOXES:
            self.box = next_box
            self.save()
