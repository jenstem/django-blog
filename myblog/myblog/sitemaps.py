from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from blog.models import Category, Post


class CategorySitemap(Sitemap):
    """
    A sitemap class that provides a list of all categories for the sitemap.
    """
    def items(self):
        """
        Returns all categories from the database.
        """
        return Category.objects.all()


class PostSitemap(Sitemap):
    """
    A sitemap class that provides a list of active posts for the sitemap.
    """
    def items(self):
        """
        Returns all active posts from the database.
        """
        return Post.objects.filter(status=Post.ACTIVE)


    def lastmod(self, obj):
        """
        Returns the last modification date of the given post object.
        """
        return obj.created_at