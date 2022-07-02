from django.urls import path

from remiolab.experiments.views import (
    ExperimentAccessView, 
    ExperimentBaseView,
    ExperimentDetailView,
    ExperimentCreateView,
    ExperimentsListView,
)

app_name = "experiments"
urlpatterns = [
    path("access/<pk>/", ExperimentAccessView.as_view(), name="access"),
    path("base/", ExperimentBaseView.as_view(), name="base"),
    path("list/", ExperimentsListView.as_view(), name="list"),
    path("create/", ExperimentCreateView.as_view(), name="create"),
    path("detail/<pk>/", ExperimentDetailView.as_view(), name="detail"),
]
