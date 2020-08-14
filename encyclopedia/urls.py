from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entryPage, name="entryPage"),
    path("random", views.randomPage, name="randomPage"),
    path("newPage", views.createNewPage, name="createNewPage"),
    path("editPage/<str:title>", views.editPage, name="editPage"),
    path("search", views.searchPage, name="searchPage")
]
