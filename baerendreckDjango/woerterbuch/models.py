from django.db import models
from django.contrib.auth import get_user_model


class Dialekt(models.Model):
    title = models.CharField("Dialekt", max_length=200)
    slug = models.SlugField("Slug", unique=True)
    description = models.TextField("Beschreibung")



class Buchstabe(models.Model):
    ...


class Wort(models.Model):
    ...
