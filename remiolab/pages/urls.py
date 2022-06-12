from django.urls import path

from remiolab.pages.views import (
    HomeView
)

app_name = "pages"
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
]
