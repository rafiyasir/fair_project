from django.db import models
from datetime import datetime
from django.urls import reverse

class Claim(models.Model):
    title = models.CharField(max_length=200)
    para_main = models.TextField()
    para_1 = models.TextField(blank=True)
    para_2 = models.TextField(blank=True)
    para_3 = models.TextField(blank=True)
    para_4 = models.TextField(blank=True)
    para_5 = models.TextField(blank=True)
    para_6 = models.TextField(blank=True)
    para_7 = models.TextField(blank=True)
    # description = models.TextField(blank=True)
    photo_main = models.ImageField(upload_to='photos/claims/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('claim', args = [str(self.id)])
