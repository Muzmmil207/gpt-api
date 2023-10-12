from django.urls import path

from . import views

urlpatterns = [
    path("", views.MessageApi.as_view()),
    path("write", views.WriteApi.as_view()),
]
