from django.urls import path
from .views import ShortenedUrlList

urlpatterns = [
    path("", ShortenedUrlList.as_view({"get": "list"}), name="short-url-list"),
    path(
        "create/",
        ShortenedUrlList.as_view({"post": "create"}),
        name="create_shortened_url",
    ),
    path(
        "<str:token>/",
        ShortenedUrlList.as_view({"get": "redirect"}),
        name="redirect_shortened_url",
    ),
]
