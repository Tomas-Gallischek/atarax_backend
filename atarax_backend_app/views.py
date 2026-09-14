from .models import Continents, Kingdom, Region, City, Dungeons, unique_location


def get_maps_data():
    print("funkce pro vypsání map - OK")
    continents = list(Continents.objects.values())
    kingdoms = list(Kingdom.objects.values())
    regions = list(Region.objects.values())
    cities = list(City.objects.values())
    dungeons = list(Dungeons.objects.values())
    unique_locations = list(unique_location.objects.values())

    return {
        "continents": continents,
        "kingdoms": kingdoms,
        "regions": regions,
        "cities": cities,
        "dungeons": dungeons,
        "unique_locations": unique_locations,
    }


# Alias pro případnou zpětnou kompatibilitu
maps = get_maps_data