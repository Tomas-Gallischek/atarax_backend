from django.db import models


class Continents(models.Model):
    name = models.CharField(max_length=150, verbose_name="Jméno")
    description = models.TextField(blank=True, null=True, verbose_name="Popis")

    class Meta:
        verbose_name = "1 - Kontinent"
        verbose_name_plural = "Kontinenty"

    def __str__(self):
        return self.name

class Kingdom(models.Model):
    name = models.CharField(max_length=150, verbose_name="Jméno")
    continent = models.ForeignKey(Continents, on_delete=models.CASCADE, verbose_name="Kontinent", blank=True, null=True)
    description = models.TextField(blank=True, null=True, verbose_name="Popis")

    class Meta:
        verbose_name = "2 - Království"
        verbose_name_plural = "Království"

    def __str__(self):
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=150, verbose_name="Jméno")
    kingdom = models.ForeignKey(Kingdom, on_delete=models.CASCADE, verbose_name="Království", blank=True, null=True)
    description = models.TextField(blank=True, null=True, verbose_name="Popis")

    class Meta:
        verbose_name = "3 - Region"
        verbose_name_plural = "Regiony"

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=150, verbose_name="Jméno")
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name="Region", blank=True, null=True)
    description = models.TextField(blank=True, null=True, verbose_name="Popis")

    class Meta:
        verbose_name = "4 - Město"
        verbose_name_plural = "Města"

    def __str__(self):
        return self.name

class Dungeons(models.Model):
    name = models.CharField(max_length=150, verbose_name="Jméno")
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name="Region", blank=True, null=True)
    description = models.TextField(blank=True, null=True, verbose_name="Popis")

    class Meta:
        verbose_name = "Dungeon"
        verbose_name_plural = "Dungeony"

    def __str__(self):
        return self.name

class unique_location(models.Model):
    name = models.CharField(max_length=150, verbose_name="Jméno")
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name="Region", blank=True, null=True)
    description = models.TextField(blank=True, null=True, verbose_name="Popis")

    class Meta:
        verbose_name = "Unikátní lokace"
        verbose_name_plural = "Unikátní lokace"

    def __str__(self):
        return self.name


class NPC(models.Model):
    name = models.CharField(max_length=150, verbose_name="Jméno")
    description = models.TextField(blank=True, null=True, verbose_name="Popis")
    city_location = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name="Město (pokud je)", blank=True, null=True)
    other_location = models.ForeignKey(unique_location, on_delete=models.CASCADE, verbose_name="Unikátní lokace (pokud je)", blank=True, null=True)
    dungeon_location = models.ForeignKey(Dungeons, on_delete=models.CASCADE, verbose_name="Dungeon (pokud je)", blank=True, null=True)

    class Meta:
        verbose_name = "NPC postava"
        verbose_name_plural = "NPC postavy"

    def __str__(self):
        return self.name

class Mobs(models.Model):
    name = models.CharField(max_length=150, verbose_name="Jméno")
    description = models.TextField(blank=True, null=True, verbose_name="Popis")

    # doplnit staty
    class Meta:
        verbose_name = "Mob"
        verbose_name_plural = "Moby"

    def __str__(self):
        return self.name