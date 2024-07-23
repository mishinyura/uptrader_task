from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)