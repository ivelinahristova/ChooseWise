from django.db import models


class Macronutrients(models.Model):
    name = models.CharField(max_length=200)
    parent = models.IntegerField(null=True, blank=True)

