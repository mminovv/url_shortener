from django.db import models
from django.utils.translation import gettext_lazy as _


class ShortenedUrl(models.Model):
    original_url = models.URLField()
    shortened_url = models.URLField()
    token = models.CharField(max_length=6, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    clicks = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = "shortened_url"
        verbose_name = _("Shortened url")
        verbose_name_plural = _("Shortened urls")

    def __str__(self):
        return f"{self.shortened_url} --> {self.original_url}"
