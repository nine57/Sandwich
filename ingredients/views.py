from rest_framework.views import APIView
from rest_framework.response import Response

from ingredients.serializers import BreadSerializer, ToppingSerializer, CheeseSerializer, SauceSerializer
from ingredients.models import Bread, Topping, Cheese, Sauce


class BreadListView(APIView):
    def get(self, request):
        breads = Bread.objects.exclude(status="deleted")
        serializer = BreadSerializer(breads, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        serializer = BreadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)


class BreadView(APIView):
    def patch(self, request, bread_id):
        if not bread_id:
            return Response({"detail": "no bread id"}, status=400)
        try:
            bread = Bread.objects.get(id=bread_id)
        except Bread.DoesNotExist:
            return Response({"detail": f"bread id {bread_id} does not exists"}, status=400)

        serializer = BreadSerializer(bread, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "SUCCESS"}, status=200)

    def delete(self, request, bread_id):
        if not bread_id:
            return Response({"detail": "no bread id"}, status=400)
        try:
            bread = Bread.objects.get(id=bread_id)
        except Bread.DoesNotExist:
            return Response({"detail": f"bread id {bread_id} does not exists"}, status=400)

        bread.status = "deleted"
        bread.save()
        return Response({"detail": "Contents Deleted"}, status=204)


class ToppingListView(APIView):
    def get(self, request):
        toppings = Topping.objects.exclude(status="deleted")
        serializer = ToppingSerializer(toppings, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        serializer = ToppingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)


class ToppingView(APIView):
    def patch(self, request, topping_id):
        if not topping_id:
            return Response({"detail": "no topping id"}, status=400)
        try:
            topping = Topping.objects.get(id=topping_id)
        except Topping.DoesNotExist:
            return Response({"detail": f"topping id {topping_id} does not exists"}, status=400)

        serializer = ToppingSerializer(
            topping, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "SUCCESS"}, status=200)

    def delete(self, request, topping_id):
        if not topping_id:
            return Response({"detail": "no topping id"}, status=400)
        try:
            topping = Topping.objects.get(id=topping_id)
        except Topping.DoesNotExist:
            return Response({"detail": f"topping id {topping_id} does not exists"}, status=400)

        topping.status = "deleted"
        topping.save()
        return Response({"detail": "Contents Deleted"}, status=204)


class CheeseListView(APIView):
    def get(self, request):
        toppings = Cheese.objects.exclude(status="deleted")
        serializer = CheeseSerializer(toppings, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        serializer = CheeseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)


class CheeseView(APIView):
    def patch(self, request, cheese_id):
        if not cheese_id:
            return Response({"detail": "no cheese id"}, status=400)
        try:
            cheese = Cheese.objects.get(id=cheese_id)
        except Cheese.DoesNotExist:
            return Response({"detail": f"cheese id {cheese_id} does not exists"}, status=400)

        serializer = CheeseSerializer(
            cheese, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "SUCCESS"}, status=200)

    def delete(self, request, cheese_id):
        if not cheese_id:
            return Response({"detail": "no cheese id"}, status=400)
        try:
            cheese = Cheese.objects.get(id=cheese_id)
        except Cheese.DoesNotExist:
            return Response({"detail": f"cheese id {cheese_id} does not exists"}, status=400)

        cheese.status = "deleted"
        cheese.save()
        return Response({"detail": "Contents Deleted"}, status=204)


class SauceListView(APIView):
    def get(self, request):
        sauces = Sauce.objects.exclude(status="deleted")
        serializer = SauceSerializer(sauces, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        serializer = SauceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)


class SauceView(APIView):
    def patch(self, request, sauce_id):
        if not sauce_id:
            return Response({"detail": "no sauce id"}, status=400)
        try:
            sauce = Sauce.objects.get(id=sauce_id)
        except Sauce.DoesNotExist:
            return Response({"detail": f"sauce id {sauce_id} does not exists"}, status=400)

        serializer = BreadSerializer(sauce, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "SUCCESS"}, status=200)

    def delete(self, request, sauce_id):
        if not sauce_id:
            return Response({"detail": "no sauce id"}, status=400)
        try:
            sauce = Sauce.objects.get(id=sauce_id)
        except Sauce.DoesNotExist:
            return Response({"detail": f"sauce id {sauce_id} does not exists"}, status=400)

        sauce.status = "deleted"
        sauce.save()
        return Response({"detail": "Contents Deleted"}, status=204)
