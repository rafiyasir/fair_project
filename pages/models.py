from django.db import models
from datetime import datetime

class Page(models.Model):
    home_header = models.CharField(max_length=150)
    home_content = models.TextField()
    consulting_content = models.TextField()
    assistance_content = models.TextField()
    queries_content = models.TextField()
    about_heading = models.CharField(max_length=150)
    about_content_1 = models.TextField()
    about_photo = models.ImageField(upload_to='photos/pages/%Y/%m/%d/')
    about_content_2 = models.TextField()
    about_content_3 = models.TextField()
    list_date = models.DateTimeField(default=datetime.now,)
