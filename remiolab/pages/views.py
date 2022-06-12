from django.views.generic import DetailView, RedirectView, UpdateView, TemplateView, CreateView


class HomeView(TemplateView):
    template_name = "pages/home.html"