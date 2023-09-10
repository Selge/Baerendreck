from django.db import models
from django.contrib.auth import get_user_model


class Dialekt(models.Model):
    title = models.CharField("Dialekt", max_length=200)
    slug = models.SlugField("Slug", unique=True)
    description = models.TextField("Beschreibung")

    class Meta:
        verbose_name_plural = 'Dialekte'

    def __str__(self):
        return self.title


class Buchstabe(models.Model):
    letter = models.CharField("Buchstabe", max_length=1)
    slug = models.SlugField("Slug", unique=True)
    def __str__(self):
        return self.letter


class Wort(models.Model):
    def __str__(self):
        return self.text
