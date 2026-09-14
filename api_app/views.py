# NAČÍTÁNÍ KNIHOVEN
from django.http import HttpRequest
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

# NAČÍTÁNÍ FUNKCÍ
from atarax_backend_app.views import get_maps_data, get_maps_detail, get_npc_data


# INDEX
@api_view(['GET'])
@permission_classes([AllowAny])
def index(request):
    print("Funkce index byla zavolána!")
    
    try:
        return Response({"message": "Index OK"}, status=status.HTTP_200_OK)

    except (TypeError, ValueError):
        return Response({"error": "Někde se stala chyba"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([AllowAny])
def maps(request: HttpRequest):
    print("Funkce maps byla zavolána!")
    
    try:
        maps_data = get_maps_data()
        print(maps_data)
        return Response(maps_data, status=status.HTTP_200_OK)
        
    except Exception as e:
        print(f"Chyba při načítání map z databáze: {e}")
        return Response(
            {"error": "Data se nepodařilo načíst", "details": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(['GET'])
@permission_classes([AllowAny])
def maps_detail(request: HttpRequest, name):
    print(f'Funkce maps_detail s parametrem {name} byla zavolána!')
    
    try:
        map_data = get_maps_detail(name)
        if map_data is None:
            return Response(
                {"error": f"Lokace '{name}' nebyla nalezena"},
                status=status.HTTP_404_NOT_FOUND
            )

        print(map_data)
        return Response(map_data, status=status.HTTP_200_OK)
        
    except Exception as e:
        print(f"Chyba při načítání map z databáze: {e}")
        return Response(
            {"error": "Data se nepodařilo načíst", "details": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    
@api_view(['GET'])
@permission_classes([AllowAny])
def npc(request: HttpRequest):
    print("Funkce npc byla zavolána!")
    
    try:
        npc_data = get_npc_data()
        print(npc_data)
        return Response(npc_data, status=status.HTTP_200_OK)
        
    except Exception as e:
        print(f"Chyba při načítání npc z databáze: {e}")
        return Response(
            {"error": "Data se nepodařilo načíst", "details": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )