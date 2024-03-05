import sqlite3
from typing import Any, Callable

from django import http
from django.db.models import F
from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from .models import Post


# @cache_page(60 * 15)
def single_post(request, slug):
    post = Post.objects.get(id=slug)

    return http.HttpResponse(post.content)


class IndexView(TemplateView):
    template_name = "blog/empty.html"

    def get(self, request: http.HttpRequest, *args: Any, **kwargs: Any) -> http.HttpResponse:
        self.upload_posts()
        return super().get(request, *args, **kwargs)

    def get_rows(self):
        con = sqlite3.connect("pickthebrain.sqlite3")
        cur = con.cursor()
        res = cur.execute("SELECT * FROM urls WHERE done = 1")
        self.rows = res.fetchall()
        cur.close()
        con.close()

    def update_posts(self, update: Callable):
        posts = Post.objects.all().exclude(id=1).order_by("id")
        for post in posts:
            update(post)

    def upload_posts(self):
        self.get_rows()

        Post.objects.bulk_create(
            [
                Post(
                    content=row[3].replace(" https://bookskai.com/sc", "/sc"),
                )
                for row in self.rows
            ],
            ignore_conflicts=True,
        )
