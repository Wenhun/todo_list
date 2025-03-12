from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from todo_list_app.forms import TaskForm
from todo_list_app.models import Task


class TaskListView(ListView):
    template_name = "todo_list_app/index.html"
    model = Task
    paginate_by = 5


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("index")


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("index")


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("index")
