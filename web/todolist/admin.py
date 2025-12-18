"""
Docstring for todolist.admin
"""

from django.contrib import admin

from .models import TodoModel


@admin.register(TodoModel)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        "id", "tg_user_id", "name", "execution_at", "created_at",
    )
    readonly_fields = (
        "tg_user_id",
    )
