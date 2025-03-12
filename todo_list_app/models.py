from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    class Meta:
        ordering = ["is_completed", "deadline"]

    content = models.TextField()
    date_created = models.DateTimeField(auto_now=True)
    deadline = models.DateField()
    is_completed = models.BooleanField(default=False)
    tag = models.ManyToManyField(
        Tag, related_name="tasks"
    )

    def __str__(self) -> str:
        return (
            f"Task completed: {self.is_completed}, Deadline={self.deadline}"
        )
