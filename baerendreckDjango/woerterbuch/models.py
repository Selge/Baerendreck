from django.db import models
from django.contrib.auth import get_user_model


class Dialekt(models.Model):
    title = models.CharField("Название", max_length=200)


class Buchstabe(models.Model):
    ...


class Wort(models.Model):
    ...
