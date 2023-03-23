from django.urls import path
from .views import redirect_shortened_url, ShortenedUrlList, create_shortened_url

urlpatterns = [
    path("all-urls/", ShortenedUrlList.as_view({"get": "list"}), name="short-url-list"),
    path("create/", create_shortened_url, name="short-url-create"),
    path("<str:shortened_url>/", redirect_shortened_url, name="short-url-redirect"),
]
