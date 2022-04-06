from rest_framework.views import APIView
from rest_framework.response import Response

from ingredients.serializers import BreadSerializer
from ingredients.models import Bread


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
        if serializer.id_valid():
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
