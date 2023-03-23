from django.db import models


class ShortenedUrl(models.Model):
    original_url = models.URLField()
    shortened_url = models.URLField()
    token = models.CharField(max_length=6, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    clicks = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.shortened_url} --> {self.original_url}"
