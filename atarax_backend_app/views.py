from .models import Location


def get_maps_data():
    print("funkce pro vypsání map - OK")
    locations = list(Location.objects.values())
    print(locations)
    return {"locations": locations}

def get_maps_detail(name):
    print(f"funkce pro vypsání detailu mapy {name} - OK")
    try:
        location = Location.objects.get(name=name)
        return {
            "id": location.id,
            "name": location.name,
            "description": location.description,
            "type": location.type,
            "continent": location.continent.name if location.continent else None,
            "kingdom": location.kingdom.name if location.kingdom else None,
            "region": location.region.name if location.region else None,
            "city": location.city.name if location.city else None,
            "specific_location": location.specific_location,
        }
    except Location.DoesNotExist:
        return None