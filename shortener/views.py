from django.shortcuts import get_object_or_404, redirect
from rest_framework import status
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet
from .models import ShortenedUrl
from .serializers import ShortenedUrlSerializer
from .utils import generate_token


class ShortenedUrlList(GenericViewSet, ListModelMixin):
    queryset = ShortenedUrl.objects.all()
    serializer_class = ShortenedUrlSerializer

    @action(detail=False, methods=["post"])
    def create(self, request):
        serializer = ShortenedUrlSerializer(data=request.data)

        if serializer.is_valid():
            token = generate_token()
            shortened_url = f"{request.get_host()}/shortener/{token}"
            serializer.save(shortened_url=shortened_url, token=token)
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=["get"])
    def redirect(self, request, token=None):
        shortened_url_obj = get_object_or_404(ShortenedUrl, token=token)
        shortened_url_obj.clicks += 1
        shortened_url_obj.save()
        return redirect(shortened_url_obj.original_url)
