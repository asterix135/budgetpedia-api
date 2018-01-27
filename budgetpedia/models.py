from django.db import models

class Default(models.Model):
    foo = models.CharField(maxlength=100, blank=True, default='')
