import time

import g4f
from django.http import StreamingHttpResponse
from g4f.Provider import (
    Acytoo,
    Aichat,
    Ails,
    ChatBase,
    ChatgptAi,
    ChatgptLogin,
    CodeLinkAva,
    H2o,
    HuggingChat,
    Opchatgpts,
    OpenaiChat,
    OpenAssistant,
    Raycast,
    Theb,
    Vercel,
    Vitalentum,
    Wewordle,
    Ylokh,
    You,
    Yqcloud,
)
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import MessageSerializer


class MessageApi(APIView):
    renderer_classes = [JSONRenderer]

    serializer_class = MessageSerializer

    def message_generator(self, message):
        response = "<!DOCTYPE html>"
        for provider in (
            Acytoo,
            Aichat,
            Ails,
            ChatgptAi,
            ChatgptLogin,
            CodeLinkAva,
            H2o,
            HuggingChat,
            Opchatgpts,
            OpenAssistant,
            OpenaiChat,
            Raycast,
            Theb,
            Vercel,
            Vitalentum,
            Wewordle,
            Ylokh,
            You,
            Yqcloud,
        ):
            try:
                response = g4f.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": message}],
                    provider=provider,
                )
            except Exception as e:
                continue
            # yield from response
            if "<!DOCTYPE html>" not in response:
                for message in response:
                    yield message
                break
        yield ""
        # return "Network Error!, Please try again."

    def get(self, request, format=None):
        usernames = []
        return Response(usernames)

    def post(self, request, format=None):
        # start = time.time()
        message = request.data.get("message", "")
        # response = self.message_generator(message)
        response = StreamingHttpResponse(
            self.message_generator(message), status=200, content_type="text/event-stream"
        )
        response["Cache-Control"] = ("no-cache",)
        # end = time.time()
        # print(f"time: {end-start}")
        return response


class WriteApi(APIView):
    renderer_classes = [JSONRenderer]

    serializer_class = MessageSerializer

    def message_generator(self, message):
        response = "<!DOCTYPE html>"
        for provider in range(10):
            try:
                response = g4f.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": message}],
                )
            except Exception as e:
                continue
            # yield from response
            if "<!DOCTYPE html>" not in response:
                lower_case = response.lower()
                if (
                    "m sorry" not in lower_case
                    and "i could" not in lower_case
                    and "i do" not in lower_case
                ):
                    return response

    def get(self, request, format=None):
        return Response("")

    def post(self, request, format=None):
        message = request.data.get("message", "")
        response = self.message_generator(message)

        return Response(response)
