from django.views.generic import DetailView, RedirectView, UpdateView, TemplateView, CreateView
from remiolab.experiments.models import Experiment


class ExperimentAccessView(TemplateView):
    template_name = "experiments/access.html"


class ExperimentBaseView(TemplateView):
    template_name = "experiments/base/index.html"


class ExperimentDetailView(DetailView):
    template_name = "experiments/detail.html"
    model = Experiment


class ExperimentCreateView(TemplateView):
    template_name = "experiments/create.html"