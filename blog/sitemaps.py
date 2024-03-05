from django.contrib.sitemaps import Sitemap

from .models import Post


class PostsSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = "https"

    def items(self):
        return Post.objects.all()

    # def lastmod(self, obj):
    #     return obj.updated_at

    def location(self, obj):
        return "/%s/" % (obj.id)
