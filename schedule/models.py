from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Tags"


class Task(models.Model):
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name="tasks")

    class Meta:
        verbose_name_plural = "Tasks"
        ordering = ["-deadline"]
