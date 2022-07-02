from django.views.generic import DetailView, ListView, UpdateView, TemplateView, CreateView
from remiolab.experiments.models import Experiment


class HomeView(ListView):
    """Home view."""
    template_name = "pages/home.html"
    model = Experiment
    paginate_by = 12
    context_object_name = "experiments"


class GalleryView(TemplateView):
    """Gallery view."""
    template_name = "pages/gallery.html"


class AboutView(TemplateView):
    """About view."""
    template_name = "pages/about.html"