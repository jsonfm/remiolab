from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PagesApp(AppConfig):
    name = "remiolab.pages"
    verbose_name = _("pages")
