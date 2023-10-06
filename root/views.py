import time

import g4f
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

# from django.http import  StreamingHttpResponse
from rest_framework.decorators import api_view
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
                return response
                # for message in response:
                #     yield message
                # break
        # yield "Network Error"
        return "Network Error!, Please try again."

    def get(self, request, format=None):

        usernames = []
        return Response(usernames)

    def post(self, request, format=None):
        # start = time.time()
        message = request.data.get("message", "")
        response = self.message_generator(message)
        # response = StreamingHttpResponse(
        #     self.message_generator(message), status=200, content_type="text/event-stream"
        # )
        # response["Cache-Control"] = ("no-cache",)
        # end = time.time()
        # print(f"time: {end-start}")
        return Response(response)
