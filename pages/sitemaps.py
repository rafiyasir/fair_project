from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from claims.models import Claim

class StaticSitemap(Sitemap):

    def items(self):
        return ['index','about', 'contactus','register','login','dashboard','logout']

    def location(self, item):
        return reverse(item)

class ClaimSitemap(Sitemap):
    def items(self):
        return Claim.objects.all()