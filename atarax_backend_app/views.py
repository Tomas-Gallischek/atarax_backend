from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import NPC, Continents, Kingdom, Region, City, Dungeons, unique_location


def maps(request):
    print("funkce pro vypsání map - OK")
    continents = Continents.objects.all()
    kingdoms = Kingdom.objects.all()
    regions = Region.objects.all()
    cities = City.objects.all()
    dungeons = Dungeons.objects.all()
    unique_locations = unique_location.objects.all()

    return ({
        "continents": continents,
        "kingdoms": kingdoms,
        "regions": regions,
        "cities": cities,
        "dungeons": dungeons,
        "unique_locations": unique_locations
    })