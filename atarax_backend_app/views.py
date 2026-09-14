from .models import Location, NPC


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

def get_npc_data():
    print("funkce pro vypsání NPC - OK")
    npc_list = list(NPC.objects.values())
    print(npc_list)
    return {"npc": npc_list}


def get_npc_detail(name):
    print(f"funkce pro vypsání detailu NPC {name} - OK")
    try:
        npc = NPC.objects.get(name=name)
        return {
            "name": npc.name,
            "description": npc.description,
            "npc_location_name": npc.npc_location_name
        }
    except NPC.DoesNotExist:
        return None