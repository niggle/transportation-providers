from django.db import models

from core.models import Language, Currency


class Provider(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    language = models.ForeignKey(Language)
    currency = models.ForeignKey(Currency)

    class Meta:
        verbose_name = "Provider"
        verbose_name_plural = "Providers"

    def __str__(self):
        return self.name
