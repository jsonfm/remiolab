from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ExperimentsApp(AppConfig):
    name = "remiolab.experiments"
    verbose_name = _("Experiments")
