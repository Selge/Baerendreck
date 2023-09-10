from django.db import models


class Dialekt(models.Model):
    title = models.TextField("Dialekt", max_length=200)
    slug = models.SlugField("Slug", unique=True, default='Deutsch')
    description = models.TextField("Beschreibung", max_length=500, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Dialekte'

    def __str__(self):
        return self.title


class Buchstabe(models.Model):
    letter = models.TextField("Buchstabe", max_length=1)
    dialect = models.ForeignKey(
        Dialekt,
        verbose_name="Dialekt",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='Buchstaben',
        help_text='Bitte, wählen Sie eine Dialekte aus'
    )

    class Meta:
        verbose_name_plural = 'Buchstaben'

    def __str__(self):
        return self.letter


class Wort(models.Model):
    text = models.TextField('Wort', max_length=300)
    uebersetzung = models.TextField('Deutsch', max_length=900)
    translation = models.TextField('Englisch', max_length=900)

    dialect = models.ForeignKey(
        Dialekt,
        verbose_name="Dialekt",
        on_delete=models.CASCADE,
        related_name='Dialekt',
        help_text='Bitte, wählen Sie eine Dialekte aus',
        blank=True,
        null=True,
    )
    letter = models.ForeignKey(
        Buchstabe,
        verbose_name="Buchstabe",
        on_delete=models.CASCADE,
        related_name='Buchstabe',
        help_text='Bitte, wählen Sie eine Buchstabe aus',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name_plural = 'Wörter'

    def __str__(self):
        return self.text
