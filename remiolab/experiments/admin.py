"""Experiments admin."""

# Django
from django.contrib import admin

# Models
from remiolab.experiments.models import Experiment

# Register your models here.
admin.site.register([Experiment])