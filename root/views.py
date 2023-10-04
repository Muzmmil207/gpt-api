import time

import g4f
from g4f.Provider import Bard, Bing

# from django.http import  StreamingHttpResponse
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import MessageSerializer


class MessageApi(APIView):
    max_try = 50

    renderer_classes = [JSONRenderer]

    serializer_class = MessageSerializer

    # def message_generator(self, message):
    #     response = "<!DOCTYPE html>"
    #     while True and self.max_try > 0:
    #         try:
    #             response = g4f.ChatCompletion.create(
    #                 model="gpt-3.5-turbo",
    #                 messages=[{"role": "user", "content": message}],
    #                 # stream=True,
    #                 provider=Bing,
    #             )
    #         except Exception as e:
    #             # print(e)
    #             self.max_try -= 1
    #             continue
    #         # yield from response
    #         if "<!DOCTYPE html>" not in response:
    #             return response
    #             # for message in response:
    #             #     yield message
    #             # break
    #         self.max_try -= 1
    #     # yield "Network Error"
    #     return "Network Error!, Please try again."
    def message_generator(self, message):
        try:
            return g4f.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": message}],
                provider=Bard,
            )
        except Exception as e:
            return g4f.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": message}],
                provider=Bing,
            )
        except:
            pass

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
