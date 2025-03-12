from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View

from todo_list_app.forms import TaskForm, TagForm
from todo_list_app.models import Task, Tag


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


class TagListView(ListView):
    model = Tag
    template_name = "todo_list_app/tag_list.html"

class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("tag-list")


class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("tag-list")


class TagDeleteView(DeleteView):
    model = Tag
    success_url = reverse_lazy("tag-list")


class ToggleTaskCompletedView(View):
    def dispatch(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        task = get_object_or_404(Task, pk=kwargs["pk"])

        if task.is_completed:
            task.is_completed = False
        else:
            task.is_completed = True

        task.save()
        return HttpResponseRedirect(
            reverse_lazy("index"))
