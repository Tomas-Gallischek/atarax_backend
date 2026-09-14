# NAČÍTÁNÍ KNIHOVEN
from django.http import HttpResponse, HttpRequest

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

# NAČÍTÁNÍ FUNKCÍ
from atarax_backend_app.views import maps


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
    
    maps_data = maps(request)

    if maps_data:
        return HttpResponse(maps_data, status=status.HTTP_200_OK)
    else:
        return HttpResponse("Data se nepodařilo načíst", status=status.HTTP_400_BAD_REQUEST)
    