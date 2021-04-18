from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="developers"),
    path("search", views.search, name="search"),
    path("details/<int:id>", views.details, name="details"),
    path("edit/<int:id>", views.edit, name="edit"),
    path("add", views.add, name="add"),
    path("delete/<int:id>", views.delete, name="delete"),
    path("weightage", views.weightage, name="weightage"),
]