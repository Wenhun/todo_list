from django import forms

from todo_list_app.models import Task, Tag


class TaskForm(forms.ModelForm):
    tag = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Task
        fields = [
            "content",
            "deadline",
            "tag"
        ]


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"
