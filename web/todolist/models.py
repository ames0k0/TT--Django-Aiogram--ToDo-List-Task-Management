from functools import partial

from django.db import models
from django.utils import timezone


def custom_id_generator(prefix: str = "core") -> str:
    """
    Docstring for custom_id_generator

    :param prefix: Description
    :type prefix: str
    :return: Description
    :rtype: str
    """
    return f"{prefix}-{timezone.now().timestamp()}"


todo_default_id = partial(custom_id_generator, prefix="user")
todo_category_default_id = partial(custom_id_generator, prefix="todo_category")


class CreatedAtMixin(models.Model):
    """
    Docstring for CreatedAtMixin
    """
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Дата создания"
    )

    class Meta:
        abstract = True


class TodoModel(CreatedAtMixin):
    """
    Docstring for Todo
    """
    id = models.CharField(
        primary_key=True,
        editable=False,
        default=todo_default_id,
        help_text="Айди задачи"
    )
    categories = models.ManyToManyField(
        "TodoCategoryModel",
        help_text="Категории задач"
    )
    tg_user_id = models.BigIntegerField(
        editable=False, blank=False, null=False,
        help_text="Айди пользователя",
    )
    name = models.CharField(
        max_length=60, blank=False, null=False,
        help_text="Название задачи",
    )
    execution_at = models.DateTimeField(
        blank=False, null=False,
        help_text="Дата исполнения таски",
    )

    class Meta:
        db_table = "todo_list"


class TodoCategoryModel(models.Model):
    """
    Docstring for TodoCategory
    """
    id = models.CharField(
        primary_key=True,
        editable=False,
        default=todo_category_default_id,
        help_text="Айди категории задач"
    )
    tg_user_id = models.BigIntegerField(
        editable=False, blank=False, null=False,
        help_text="Айди пользователя",
    )
    name = models.CharField(
        max_length=60, blank=False, null=False,
        help_text="Название категории задач",
    )

    class Meta:
        db_table = "todo_list_category"
