from .models import Location


def get_maps_data():
    print("funkce pro vypsání map - OK")
    locations = list(Location.objects.values())
    print(locations)
    return {"locations": locations}

