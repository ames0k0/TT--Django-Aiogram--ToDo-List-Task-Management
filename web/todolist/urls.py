"""
Docstring for todolist.urls
"""

from django.urls import path

from .views import TodoView
from .views import TodoCategoryView


urlpatterns = [
    path("todo/", TodoView.as_view()),
    path("todo-category/", TodoCategoryView.as_view()),
]
