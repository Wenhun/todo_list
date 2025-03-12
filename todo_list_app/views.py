from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from todo_list_app.models import Task


class IndexView(ListView):
    template_name = "todo_list/index.html"
    model = Task
    paginate_by = 5
