from django.urls import path

from remiolab.pages.views import (
    HomeView,
    AboutView,
    GalleryView,
)

app_name = "pages"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("/gallery", GalleryView.as_view(), name="gallery"),
    path("/about", AboutView.as_view(), name="about"),
]
