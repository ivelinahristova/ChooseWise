from django.db import models
from django.contrib.auth.models import User

class Alergens(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Nutrient_Categories(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Nutrients(models.Model):
    nutrient_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    parent = models.ForeignKey('self', null=True, blank=True)
    category = models.ForeignKey(Nutrient_Categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Foods(models.Model):
    food_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    alergens = models.ManyToManyField(Alergens, null=True, blank=True)

    def __str__(self):
        return self.name

class Foods_Nutrients(models.Model):
    nutrient = models.ForeignKey(Nutrients, on_delete=models.CASCADE)
    food = models.ForeignKey(Foods, on_delete=models.CASCADE)
    grams = models.IntegerField() #Per 100gr food

    class Meta:
        unique_together = (("nutrient", "food"),)

class ConsumedProducts(models.Model):
    date = models.DateField()
    food = models.ForeignKey(Foods, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    count = models.IntegerField() #per 100 grams

    def __str__(self):
        return self.user + self.user

class Diet(models.Model):
    nutrient = models.ForeignKey(Nutrients, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    grams = models.IntegerField() #per day

    def __str__(self):
        return self.nutrient

    class Meta:
        unique_together = (("nutrient", "user"),)
