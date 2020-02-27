from django.db import models


# Create your models here.
class Continent(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Law(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=150)
    continent = models.ForeignKey(Continent, on_delete=models.SET_NULL, null=True, blank=True)
    law = models.ForeignKey(Law, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name_plural = "countries"

    def __str__(self):
        return self.name
