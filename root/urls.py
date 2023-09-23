from django.urls import path

from . import views

urlpatterns = [
    path("", views.get_routes),
    path("messages", views.messages, name="messages-api"),
]
