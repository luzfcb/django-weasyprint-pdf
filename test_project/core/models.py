from django.db import models


# Create your models here.
class TestModel(models.Model):
    header = models.TextField(blank=True, default='')
    content = models.TextField(blank=True, default='')
    footer = models.TextField(blank=True, default='')

