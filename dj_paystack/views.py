from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from dj_paystack.models import Webhook
from dj_paystack.serializer import WebhookSerializer


class WebhookView(APIView):

    def get(self, request, *args, **kwargs):
        users = Webhook.objects.all()
        singlItem = users.first()
        # serialize = UserSerializer(users, many=True) #Serializing multiple items
        serialize = WebhookSerializer(singlItem)
        return Response(serialize.data)

    def post(self, request, *args, **kwargs):
        serialize = WebhookSerializer(data=request.data,)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        return Response(serialize.errors)
