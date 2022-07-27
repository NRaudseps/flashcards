# DJANGO
from django.contrib import admin

from . import models


class BoxAdmin(admin.ModelAdmin):
    pass


class FlashcardAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Box)
admin.site.register(models.FlashCard)
