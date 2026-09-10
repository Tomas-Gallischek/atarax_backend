from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import NPC, Continents, Kingdom, Region, City, Dungeons, unique_location


@api_view(['GET'])
def get_npcs(request):
    """
    Vrati seznam vsech NPC postav.
    """
    npcs = NPC.objects.all()
    data = [
        {
            "id": npc.id,
            "name": npc.name,
        }
        for npc in npcs
    ]
    return Response(data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_all_locations(request):
    """
    Vrati vsechny lokace rozdelene podle typu.
    """
    data = {
        "continents": [
            {"id": c.id, "name": c.name, "description": c.description}
            for c in Continents.objects.all()
        ],
        "kingdoms": [
            {"id": k.id, "name": k.name, "continent_id": k.continent_id, "description": k.description}
            for k in Kingdom.objects.all()
        ],
        "regions": [
            {"id": r.id, "name": r.name, "kingdom_id": r.kingdom_id, "description": r.description}
            for r in Region.objects.all()
        ],
        "cities": [
            {"id": c.id, "name": c.name, "region_id": c.region_id, "description": c.description}
            for c in City.objects.all()
        ],
        "dungeons": [
            {"id": d.id, "name": d.name, "region_id": d.region_id, "description": d.description}
            for d in Dungeons.objects.all()
        ],
        "unique_locations": [
            {"id": u.id, "name": u.name, "region_id": u.region_id, "description": u.description}
            for u in unique_location.objects.all()
        ],
    }

    return Response(data, status=status.HTTP_200_OK)

