from django.shortcuts import render
from django.views.generic import TemplateView

from todo_list_app.models import Task


class IndexView(TemplateView):
    template_name = "todo_list/index.html"

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        tasks = Task.objects.prefetch_related("tags").all()

        context.update(
            {
                "tasks": tasks,
            }
        )

        return context
