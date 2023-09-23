from django.urls import path

from . import views

urlpatterns = [
    path("", views.MessageApi.as_view()),
    path("dfdf", views.get_routes),
    path("messages", views.messages, name="messages-api"),
]
