# NAČÍTÁNÍ KNIHOVEN
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny




# INDEX
@api_view(['GET'])
@permission_classes([AllowAny])
def index(request):
    print("Funkce index byla zavolána!")
    
    try:
        return Response({"message": "Index OK"}, status=status.HTTP_200_OK)

    except (TypeError, ValueError):
        return Response({"error": "Někde se stala chyba"}, status=status.HTTP_400_BAD_REQUEST)