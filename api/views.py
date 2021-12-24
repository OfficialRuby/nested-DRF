from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import CarBrand
from api.serializer import CarBrandSerializer


class CarBrandView(APIView):
    # permission_classes = [IsAuthenticated, ]

    def get(self, request, *args, **kwargs):
        users = CarBrand.objects.all()
        singlItem = users.first()
        # serialize = UserSerializer(users, many=True) #Serializing multiple items
        serialize = CarBrandSerializer(singlItem)

        return Response(serialize.data)

    def post(self, request, *args, **kwargs):
        serialize = CarBrandSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        return Response(serialize.errors)
