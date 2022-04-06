import json
from rest_framework.views import APIView
from rest_framework.response import Response

from sandwiches.serializers import SandwichSerializer
from sandwiches.models import Sandwich
from ingredients.models import Bread, Topping, Cheese, Sauce


class SandwichListView(APIView):
    def get(self, request):
        # get query parameter => filtering, pagination
        sandwiches = Sandwich.objects.exclude(status="deleted")
        serializer = SandwichSerializer(sandwiches, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        serializer = SandwichSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class SandwichView(APIView):
    def delete(self, request, sandwich_id):
        if not sandwich_id:
            return Response({"detail": "no sandwich_id"}, status=400)
        try:
            sandwich = Sandwich.objects.get(id=sandwich_id)
        except Sandwich.DoesNotExist:
            return Response({"detail": f"sandwich id {sandwich_id} does not exists"}, status=400)

        sandwich.status = "deleted"
        sandwich.save()
        return Response({"detail": "Contents Deleted"}, status=204)
