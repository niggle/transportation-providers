from django.contrib.gis.db import models

from providers.models import Provider


class ServiceArea(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    provider = models.ForeignKey(Provider)

    area = models.PolygonField(srid=4326)
    objects = models.GeoManager()

    class Meta:
        verbose_name = "Service Area"
        verbose_name_plural = "Service Areas"

    def __str__(self):
        return self.name
