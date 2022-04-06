from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from sandwiches.serializers import SandwichSerializer
from sandwiches.models import Sandwich
from ingredients.models import Bread, Topping, Cheese, Sauce


class SandwichListView(APIView):
    @swagger_auto_schema(responses={200: SandwichSerializer},
                         operation_description="GET list of sandwich")
    def get(self, request):
        query_para = request.GET
        bread = query_para.get("bread", None)
        topping = query_para.getlist("topping", None)
        cheese = query_para.get("cheese", None)
        sauce = query_para.getlist("sauce", None)
        offset = int(query_para.get("offset", 0))
        limit = int(query_para.get("limit", 10))
        price = int(query_para.get("price", None))

        filtering = Q()
        if bread:
            filtering &= Q(bread_id=bread)
        if topping:
            filtering &= Q(toppings__in=topping)
        if cheese:
            filtering &= Q(cheese_id=cheese)
        if sauce:
            filtering &= Q(sauces__in=sauce)
        if price < 0:
            filtering &= Q(price__lte=-price)
        elif price > 0:
            filtering &= Q(price__gte=price)

        sandwiches = Sandwich.objects.filter(filtering).exclude(
            status="deleted").distinct()[offset*limit:(offset+1)*limit]
        serializer = SandwichSerializer(sandwiches, many=True)

        return Response(serializer.data, status=200)

    @swagger_auto_schema(request_body=SandwichSerializer,
                         responses={201: "success"},
                         operation_description="POST sandwich (making)")
    def post(self, request):
        serializer = SandwichSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class SandwichView(APIView):
    def patch(self, request, sandwich_id):
        if not sandwich_id:
            return Response({"detail": "no sandwich_id"}, status=400)
        try:
            sandwich = Sandwich.objects.get(id=sandwich_id)
        except Sandwich.DoesNotExist:
            return Response({
                "detail": f"sandwich id {sandwich_id} does not exists"},
                status=400)

    @swagger_auto_schema(responses={204: "Contents Deleted"},
                         operation_description="DELETE sandwich data")
    def delete(self, request, sandwich_id):
        if not sandwich_id:
            return Response({"detail": "no sandwich_id"}, status=400)
        try:
            sandwich = Sandwich.objects.get(id=sandwich_id)
        except Sandwich.DoesNotExist:
            return Response({
                "detail": f"sandwich id {sandwich_id} does not exists"},
                status=400)

        sandwich.status = "deleted"
        sandwich.save()
        return Response({"detail": "Contents Deleted"}, status=204)
