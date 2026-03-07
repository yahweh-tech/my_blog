from django.db import models
from datetime import datetime

class Blog(models.Model):
    title=models.CharField(max_length=50)
    blog_body=models.CharField(max_length=500)
    created_date=models.DateTimeField(default=datetime.now,blank=True)

