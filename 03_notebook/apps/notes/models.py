from django.db import models


class Note(models.Model):

    title = models.CharField(max_length=150)
    desctiption = models.TextField()
    tag = models.JSONField(default=list, blank=True)
    image = models.ImageField(upload_to="notes/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Note"
        verbose_name_plural = "Notes"

    def __str__(self):
        return f"{self.name} - {self.subject}"
