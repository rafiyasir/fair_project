from django.db import models
from datetime import datetime
from django.urls import reverse

class Claim(models.Model):
    title = models.CharField(max_length=200)
    point_main = models.CharField(max_length=200)
    point_1 = models.CharField(max_length=200, blank=True)
    point_2 = models.CharField(max_length=200, blank=True)
    point_3 = models.CharField(max_length=200, blank=True)
    point_4 = models.CharField(max_length=200, blank=True)
    point_5 = models.CharField(max_length=200, blank=True)
    point_6 = models.CharField(max_length=200, blank=True)
    point_7 = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    photo_main = models.ImageField(upload_to='photos/claims/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('claim', args = [str(self.id)])
