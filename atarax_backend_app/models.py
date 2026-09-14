from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=150, verbose_name="Jméno")
    description = models.TextField(blank=True, null=True, verbose_name="Popis")

    LOCATION_TYPE_CHOICES = (
        ("kontinent", "Kontinent"),
        ("království", "Království"),
        ("region", "Region"),
        ("město", "Město"),
        ("specifická lokace", "Specifická lokace"),
    )
    type = models.CharField(max_length=100, verbose_name="Typ", choices=LOCATION_TYPE_CHOICES)

    continent = models.CharField(max_length=150, verbose_name="Kontinent", blank=True, null=True)
    kingdom = models.CharField(max_length=150, verbose_name="Království", blank=True, null=True)
    region = models.CharField(max_length=150, verbose_name="Region", blank=True, null=True)
    city = models.CharField(max_length=150, verbose_name="Město", blank=True, null=True)
    specific_location = models.CharField(max_length=150, verbose_name="Specifická lokace", blank=True, null=True)
    
    class Meta:
        verbose_name = "Lokace"
        verbose_name_plural = "Lokace"

    def __str__(self):
        return self.name