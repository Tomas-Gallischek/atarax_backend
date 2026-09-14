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

    continent = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name="Kontinent", blank=True, null=True, related_name="continent_locations")
    kingdom = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name="Království", blank=True, null=True, related_name="kingdom_locations")
    region = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name="Region", blank=True, null=True, related_name="region_locations")
    city = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name="Město", blank=True, null=True, related_name="city_locations")
    specific_location = models.CharField(max_length=150, verbose_name="Specifická lokace", blank=True, null=True)
    
    class Meta:
        verbose_name = "Lokace"
        verbose_name_plural = "Lokace"

    def __str__(self):
        return self.name

class NPC(models.Model):

    name = models.CharField(max_length=150, verbose_name="Jméno")
    description = models.TextField(blank=True, null=True, verbose_name="Popis")
    npc_location = models.ForeignKey(Location, on_delete=models.CASCADE, verbose_name="Lokace", blank=True, null=True, related_name="npc_locations")
    
    class Meta:
        verbose_name = "NPC"
        verbose_name_plural = "NPC"

    def __str__(self):
        return self.name