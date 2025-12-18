"""
Docstring for todolist.views
"""

from django.http import JsonResponse
from django.views import View

from .models import TodoModel
from .models import TodoCategoryModel


class TodoView(View):
    """
    Docstring for TodoView
    """

    def post(self, request, *args, **kwargs):
        """
        `CREATE` Todo Task

        QueryParams
        -----------
        tg_user_id: BigInt - Telegram User `char_id`
        name: str - Todo name
        todo_category_ids: str - TodoCategory ids to bind seperated by ','
        execution_at: dt - Todo Task execution datetime
        """
        print(request.GET)
        # NOTE: Won't validate here (bot service) have to validate
        name = request.GET.get("name")
        tg_user_id = request.GET.get("tg_user_id")
        tg_user_id = int(tg_user_id)
        todo_category_ids = request.GET.get("todo_category_ids")
        todo_category_ids = todo_category_ids.split(",")
        execution_at = request.GET.get("execution_at")

        print(tg_user_id)
        print(name)
        print(todo_category_ids)
        print(execution_at)

        model = TodoModel(
            tg_user_id=tg_user_id,
            name=name,
            execution_at=execution_at,
        )
        # model.categories.set(todo_category_ids)
        model.save()

        return JsonResponse({
            "status": "success",
            "message": f"Todo(id={model.id}) created!",
            "data": {
                "id": model.id,
            }
        })


        return JsonResponse(model.__dict__)

    def get(self, request, *args, **kwargs):
        """
        `READ` Todo Task

        :param self: Description
        :param request: Description
        :param args: Description
        :param kwargs: Description
        """
        return JsonResponse({
            "msg": "h-TodoView",
        })

    def patch(self, request, *args, **kwargs):
        """
        `UPDATE` Todo Task

        :param self: Description
        :param request: Description
        :param args: Description
        :param kwargs: Description
        """

    def delete(self, request, *args, **kwargs):
        """
        `DELETE` Todo Task

        :param self: Description
        :param request: Description
        :param args: Description
        :param kwargs: Description
        """


class TodoCategoryView(View):
    """
    Docstring for TodoCategoryView
    """

    def post(self, request, *args, **kwargs):
        """
        `CREATE` Todo Task Category

        :param self: Description
        :param request: Description
        :param args: Description
        :param kwargs: Description
        """

    def get(self, request, *args, **kwargs):
        """
        `READ` Todo Task Category

        :param self: Description
        :param request: Description
        :param args: Description
        :param kwargs: Description
        """
        return JsonResponse({
            "msg": "h-TodoView",
        })

    def patch(self, request, *args, **kwargs):
        """
        `UPDATE` Todo Task Category

        :param self: Description
        :param request: Description
        :param args: Description
        :param kwargs: Description
        """

    def delete(self, request, *args, **kwargs):
        """
        `DELETE` Todo Task Category

        :param self: Description
        :param request: Description
        :param args: Description
        :param kwargs: Description
        """
