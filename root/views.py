import json

import g4f
from django.contrib.auth.models import User
from rest_framework import authentication, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from .serializers import MessageSerializer


class MessageApi(APIView):

    serializer_class = MessageSerializer

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = []
        return Response(usernames)

    def post(self, request, format=None):
        message = request.data.get("message", "")
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": message}],
        )
        data = {"message": response}
        return Response(data)


@api_view(["GET"])
def get_routes(request):

    return Response({})


@api_view(["POST", "GET"])
def messages(request):
    message = request.data.get("message", "")
    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message}],
    )
    data = {"data": response}
    return Response(data)
