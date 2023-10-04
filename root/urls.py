from django.urls import path

from . import views

urlpatterns = [
    path("", views.MessageApi.as_view()),
]
