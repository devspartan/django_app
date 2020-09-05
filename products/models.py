from django.db import models

# Create your models here.
class Products(models.Model):
    title = models.TextField()
    desc = models.TextField()
    price = models.TextField()
    summary = models.TextField()