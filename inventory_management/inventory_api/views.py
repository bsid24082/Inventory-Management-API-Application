from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Item
from .serializers import ItemSerializer

class ItemDetails(APIView):
    def get(self, request, name):
        try:
            item = Item.objects.get(name=name)  # Fetch item based on name
            serializer = ItemSerializer(item)
            return Response(serializer.data)
        except Item.DoesNotExist:
            return Response({"message": "Item not found"}, status=status.HTTP_404_NOT_FOUND)
