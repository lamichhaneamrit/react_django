from django.db import models
from datetime import datetime # importing  datetime at the time of adding content

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(default =datetime.now, blank= True)

