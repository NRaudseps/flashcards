# DJANGO
from django.contrib import admin

from . import models


class FlashcardAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.FlashCard)
