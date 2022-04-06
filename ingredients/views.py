from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from ingredients.serializers import (
    BreadSerializer,
    ToppingSerializer,
    CheeseSerializer,
    SauceSerializer)
from ingredients.models import Bread, Topping, Cheese, Sauce


class BreadListView(APIView):
    @swagger_auto_schema(responses={200: BreadSerializer},
                         operation_description="GET list of bread")
    def get(self, request):
        breads = Bread.objects.exclude(status="deleted")
        serializer = BreadSerializer(breads, many=True)
        return Response(serializer.data, status=200)

    @swagger_auto_schema(request_body=BreadSerializer,
                         responses={201: "success"},
                         operation_description="POST bread data")
    def post(self, request):
        serializer = BreadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)


class BreadView(APIView):
    @swagger_auto_schema(request_body=BreadSerializer,
                         responses={200: "success"},
                         operation_description="PATCH bread data")
    def patch(self, request, bread_id):
        if not bread_id:
            return Response({"detail": "no bread id"}, status=400)
        try:
            bread = Bread.objects.get(id=bread_id)
        except Bread.DoesNotExist:
            return Response({
                "detail": f"bread id {bread_id} does not exists"}, status=400)
        serializer = BreadSerializer(bread, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "SUCCESS"}, status=200)

    @swagger_auto_schema(responses={204: "Contents Deleted"},
                         operation_description="DELETE bread data")
    def delete(self, request, bread_id):
        if not bread_id:
            return Response({"detail": "no bread id"}, status=400)
        try:
            bread = Bread.objects.get(id=bread_id)
        except Bread.DoesNotExist:
            return Response({
                "detail": f"bread id {bread_id} does not exists"}, status=400)

        bread.status = "deleted"
        bread.save()
        return Response({"detail": "Contents Deleted"}, status=204)


class ToppingListView(APIView):
    @swagger_auto_schema(responses={200: BreadSerializer},
                         operation_description="GET list of toppings")
    def get(self, request):
        toppings = Topping.objects.exclude(status="deleted")
        serializer = ToppingSerializer(toppings, many=True)
        return Response(serializer.data, status=200)

    @swagger_auto_schema(request_body=ToppingSerializer,
                         responses={201: "success"},
                         operation_description="POST topping data")
    def post(self, request):
        serializer = ToppingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)


class ToppingView(APIView):
    @swagger_auto_schema(request_body=ToppingSerializer,
                         responses={200: "success"},
                         operation_description="PATCH topping data")
    def patch(self, request, topping_id):
        if not topping_id:
            return Response({"detail": "no topping id"}, status=400)
        try:
            topping = Topping.objects.get(id=topping_id)
        except Topping.DoesNotExist:
            return Response({
                "detail": f"topping id {topping_id} does not exists"},
                status=400)

        serializer = ToppingSerializer(
            topping, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "SUCCESS"}, status=200)

    @swagger_auto_schema(responses={204: "Contents Deleted"},
                         operation_description="DELETE topping data")
    def delete(self, request, topping_id):
        if not topping_id:
            return Response({"detail": "no topping id"}, status=400)
        try:
            topping = Topping.objects.get(id=topping_id)
        except Topping.DoesNotExist:
            return Response({
                "detail": f"topping id {topping_id} does not exists"},
                status=400)

        topping.status = "deleted"
        topping.save()
        return Response({"detail": "Contents Deleted"}, status=204)


class CheeseListView(APIView):
    @swagger_auto_schema(responses={200: CheeseSerializer},
                         operation_description="GET list of cheese")
    def get(self, request):
        cheese = Cheese.objects.exclude(status="deleted")
        serializer = CheeseSerializer(cheese, many=True)
        return Response(serializer.data, status=200)

    @swagger_auto_schema(request_body=CheeseSerializer,
                         responses={201: "success"},
                         operation_description="POST cheese data")
    def post(self, request):
        serializer = CheeseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)


class CheeseView(APIView):
    @swagger_auto_schema(request_body=CheeseSerializer,
                         responses={200: "success"},
                         operation_description="PATCH cheese data")
    def patch(self, request, cheese_id):
        if not cheese_id:
            return Response({"detail": "no cheese id"}, status=400)
        try:
            cheese = Cheese.objects.get(id=cheese_id)
        except Cheese.DoesNotExist:
            return Response({
                "detail": f"cheese id {cheese_id} does not exists"},
                status=400)

        serializer = CheeseSerializer(
            cheese, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "SUCCESS"}, status=200)

    @swagger_auto_schema(responses={204: "Contents Deleted"},
                         operation_description="DELETE cheese data")
    def delete(self, request, cheese_id):
        if not cheese_id:
            return Response({"detail": "no cheese id"}, status=400)
        try:
            cheese = Cheese.objects.get(id=cheese_id)
        except Cheese.DoesNotExist:
            return Response({
                "detail": f"cheese id {cheese_id} does not exists"},
                status=400)

        cheese.status = "deleted"
        cheese.save()
        return Response({"detail": "Contents Deleted"}, status=204)


class SauceListView(APIView):
    @swagger_auto_schema(responses={200: SauceSerializer},
                         operation_description="GET list of sauces")
    def get(self, request):
        sauces = Sauce.objects.exclude(status="deleted")
        serializer = SauceSerializer(sauces, many=True)
        return Response(serializer.data, status=200)

    @swagger_auto_schema(request_body=SauceSerializer,
                         responses={201: "success"},
                         operation_description="POST sauces data")
    def post(self, request):
        serializer = SauceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)


class SauceView(APIView):
    @swagger_auto_schema(request_body=SauceSerializer,
                         responses={200: "success"},
                         operation_description="PATCH sauce data")
    def patch(self, request, sauce_id):
        if not sauce_id:
            return Response({"detail": "no sauce id"}, status=400)
        try:
            sauce = Sauce.objects.get(id=sauce_id)
        except Sauce.DoesNotExist:
            return Response({
                "detail": f"sauce id {sauce_id} does not exists"},
                status=400)

        serializer = SauceSerializer(sauce, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "SUCCESS"}, status=200)

    @swagger_auto_schema(responses={204: "Contents Deleted"},
                         operation_description="DELETE sauce data")
    def delete(self, request, sauce_id):
        if not sauce_id:
            return Response({"detail": "no sauce id"}, status=400)
        try:
            sauce = Sauce.objects.get(id=sauce_id)
        except Sauce.DoesNotExist:
            return Response({
                "detail": f"sauce id {sauce_id} does not exists"}, status=400)

        sauce.status = "deleted"
        sauce.save()
        return Response({"detail": "Contents Deleted"}, status=204)
