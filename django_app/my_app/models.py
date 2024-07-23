from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

class Link(models.Model):
    parent = models.ForeignKey('Link', on_delete=models.CASCADE, null=True, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    url = models.CharField(max_length=255, null=False, blank=True)