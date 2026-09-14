# NAČÍTÁNÍ KNIHOVEN
from django.http import HttpRequest
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

# NAČÍTÁNÍ FUNKCÍ
from atarax_backend_app.views import get_maps_data

# pyrefly: ignore [missing-import]
from atarax_backend_app.models import Continents

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



    
