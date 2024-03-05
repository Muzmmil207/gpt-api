from django.urls import path

from . import views

urlpatterns = [
    path("upload/", views.IndexView.as_view(), name="upload-post"),
    path("<slug:slug>/", views.single_post, name="single-post"),
]
