# DJANGO
from django.urls import path

from . import views

app_name = "flashcards"

urlpatterns = [
    path("", views.index, name="index"),
    path("new/", views.new, name="new"),
    path("create/", views.create, name="create"),
    path("edit/<int:pk>", views.edit, name="edit"),
    path("update/", views.update, name="update"),
    path("box/<int:pk>", views.box, name="box"),
    path("quiz/", views.quiz, name="quiz"),
]
