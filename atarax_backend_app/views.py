from .models import Location


def get_maps_data():
    print("funkce pro vypsání map - OK")
    locations = list(Location.objects.values())
    print(locations)
    return {"locations": locations}

def get_maps_detail(name):
    print(f"funkce pro vypsání detailu mapy {name} - OK")
    map_name = name
    map_data = Location.objects.get(name=map_name)
    print(map_data)
    return {"map_data": map_data}