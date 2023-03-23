import secrets

from django.shortcuts import get_object_or_404
from django.http import Http404
from django.shortcuts import redirect
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import ShortenedUrl
from .serializers import ShortenedUrlSerializer
from rest_framework.viewsets import GenericViewSet


class ShortenedUrlList(GenericViewSet, ListModelMixin):
    queryset = ShortenedUrl.objects.all()
    serializer_class = ShortenedUrlSerializer


@extend_schema(
    request=ShortenedUrlSerializer,
    responses={201: ShortenedUrlSerializer}
)
@api_view(["POST"])
def create_shortened_url(request):
    serializer = ShortenedUrlSerializer(data=request.data)
    if serializer.is_valid():
        shortened_url = secrets.token_urlsafe(4)[:6]
        while ShortenedUrl.objects.filter(shortened_url=shortened_url).exists():
            shortened_url = secrets.token_urlsafe(4)[:6]
        serializer.save(shortened_url=shortened_url)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def redirect_shortened_url(request, shortened_url):
    try:
        shortened_url = get_object_or_404(ShortenedUrl, shortened_url=shortened_url)
        shortened_url.clicks += 1
        shortened_url.save()
        return redirect(shortened_url.original_url)
    except Http404:
        return Response(
            {"error": "Shortened URL does not exist"}, status=status.HTTP_404_NOT_FOUND
        )
