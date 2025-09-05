from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import GroceryResponseSerializer, GroceryRequestSerializer
from .models import Grocery


# 1. List All Groceries
class GroceryListView(APIView):
    def get(self, request, *args, **kwargs):
        groceries = Grocery.objects.all()
        serializer = GroceryResponseSerializer(groceries, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# 2. Create Grocery
class GroceryCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = GroceryRequestSerializer(data=request.data)
        if serializer.is_valid():
            grocery = Grocery.objects.create(**serializer.validated_data)
            response_serializer = GroceryResponseSerializer(grocery)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 3. Update Grocery
class GroceryUpdateView(APIView):
    def put(self, request, pk, *args, **kwargs):
        try:
            grocery = Grocery.objects.get(pk=pk)
        except Grocery.DoesNotExist:
            return Response({"error": "Grocery id not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = GroceryRequestSerializer(data=request.data)
        if serializer.is_valid():
            grocery.name = serializer.validated_data['name']
            grocery.price = serializer.validated_data['price']
            grocery.rating = serializer.validated_data['rating']
            grocery.save()

            response_serializer = GroceryResponseSerializer(grocery)
            return Response(response_serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 4. Delete Grocery
class GroceryDeleteView(APIView):
    def delete(self, request, pk, *args, **kwargs):
        try:
            grocery = Grocery.objects.get(pk=pk)
        except Grocery.DoesNotExist:
            return Response({"error": "Grocery id not found"}, status=status.HTTP_404_NOT_FOUND)

        grocery.delete()
        return Response({"message": "Deleted successfully"}, status=status.HTTP_200_OK)
3ghuughuh

# 5. Search Grocery by Name
class GrocerySearchView(APIView):
    def get(self, request, *args, **kwargs):
        query_name = request.query_params.get("name", "")
        groceries = Grocery.objects.filter(name__icontains=query_name)
        serializer = GroceryResponseSerializer(groceries, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
