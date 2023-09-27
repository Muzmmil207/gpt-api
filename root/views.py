import json

import g4f
from django.contrib.auth.models import User
from django.http import JsonResponse, StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import authentication, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from .serializers import MessageSerializer


class MessageApi(APIView):
    max_try = 50

    serializer_class = MessageSerializer

    def get(self, request, format=None):

        usernames = []
        return Response(usernames)

    def post(self, request, format=None):
        message = request.data.get("message", "")

        while True and self.max_try > 0:
            try:
                response = g4f.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": message}],
                )
            except:
                self.max_try -= 1
                continue

            if "<!DOCTYPE html>" not in response:
                data = {"message": response}
                return Response(data)

            self.max_try -= 1
        data = {"message": "Network Error"}
        return Response(data)


class MessageApi(APIView):
    max_try = 50

    renderer_classes = [JSONRenderer]

    serializer_class = MessageSerializer

    def message_generator(self, message):
        response = "<!DOCTYPE html>"
        while True and self.max_try > 0:
            try:
                response = g4f.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": message}],
                    stream=True,
                )
            except Exception as e:
                print(e)
                self.max_try -= 1
                continue

            for message in response:
                yield message
            break
            self.max_try -= 1
        # yield "Network Error"

    def get(self, request, format=None):

        usernames = []
        return Response(usernames)

    def post(self, request, format=None):
        message = request.data.get("message", "")
        # message = self.message_generator(message)
        response = StreamingHttpResponse(
            self.message_generator(message), status=200, content_type="text/event-stream"
        )
        response["Cache-Control"] = ("no-cache",)
        return response


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
