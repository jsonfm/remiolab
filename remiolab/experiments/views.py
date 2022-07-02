from django.views.generic import ListView, DetailView, RedirectView, UpdateView, TemplateView, CreateView
from remiolab.experiments.models import Experiment


class ExperimentAccessView(DetailView):
    template_name = "experiments/access.html"
    model = Experiment
    context_object_name = "experiment"


class ExperimentBaseView(TemplateView):
    template_name = "experiments/base/index.html"


class ExperimentDetailView(DetailView):
    template_name = "experiments/detail.html"
    model = Experiment


class ExperimentCreateView(TemplateView):
    template_name = "experiments/create.html"


class ExperimentsListView(ListView):
    template_name = "experiments/list.html"
    model = Experiment
    paginate_by = 12
    context_object_name = "experiments"