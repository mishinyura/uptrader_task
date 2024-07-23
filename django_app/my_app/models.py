from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    link = models.ManyToManyField('Link')

class Link(models.Model):
    parent = models.ForeignKey('Link', on_delete=models.CASCADE, null=True, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    url = models.CharField(max_length=255, null=False, blank=True)
    position = models.PositiveSmallIntegerField(null=False, blank=True, default=0)
