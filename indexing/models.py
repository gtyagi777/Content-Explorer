from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Link(models.Model):
    url = models.URLField(unique=True)

class Bookmark(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User,on_delete=models.PROTECT)
    link = models.ForeignKey(Link,on_delete=models.PROTECT)