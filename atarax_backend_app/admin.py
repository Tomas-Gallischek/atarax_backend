from django.contrib import admin
from .models import NPC, Continents, Kingdom, Region, City, Dungeons, unique_location, Mobs

@admin.register(Continents)
class ContinentsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)

@admin.register(Kingdom)
class KingdomAdmin(admin.ModelAdmin):
    list_display = ('name', 'continent')
    list_filter = ('name', 'continent')

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('name', 'kingdom')
    list_filter = ('name', 'kingdom')

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'region')
    list_filter = ('name', 'region')

@admin.register(Dungeons)
class DungeonsAdmin(admin.ModelAdmin):
    list_display = ('name', 'region')
    list_filter = ('name', 'region')

@admin.register(unique_location)
class unique_locationAdmin(admin.ModelAdmin):
    list_display = ('name', 'region')
    list_filter = ('name', 'region')

@admin.register(NPC)
class NPCAdmin(admin.ModelAdmin):
    list_display = ('name', 'city_location', 'dungeon_location', 'other_location')
    list_filter = ('name', 'city_location', 'dungeon_location', 'other_location')

@admin.register(Mobs)
class MobsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)