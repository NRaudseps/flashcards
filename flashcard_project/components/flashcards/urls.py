from django.urls import path

from . import views

app_name = "flashcard_project"

urlpatterns = [path("", views.index)]