from django.db import models


class Experiment(models.Model):
    name = models.CharField(max_length=255, blank=True)
    description = models.TextField(max_length=500, blank=True)
    html = models.TextField(blank=True)
    js = models.TextField(blank=True)
    constants = models.TextField(blank=True)
    utils = models.TextField(blank=True)
    dependencies = models.TextField(blank=True)
    css = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name