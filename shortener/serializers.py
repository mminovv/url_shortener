from rest_framework import serializers
from .models import ShortenedUrl


class ShortenedUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortenedUrl
        fields = (
            "original_url",
            "shortened_url",
            "created",
            "clicks",
        )
        read_only_fields = ("created", "clicks", "shortened_url")
