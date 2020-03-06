from django.db import models


# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=150)
    flag_image = models.ImageField(upload_to='flags/')

    class Meta:
        verbose_name_plural = "countries"

    def __str__(self):
        return self.name


class Law(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=250)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='laws/')

    def __str__(self):
        return self.title

class Right(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=150)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='rights/')

    def __str__(self):
        return self.title
