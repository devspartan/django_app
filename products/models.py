from django.db import models
import datetime

# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=120)
    desc = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    mail = models.EmailField(default="abc@gmail.com")
    check = models.BooleanField(default=False)
    dt = models.DateField(default=datetime.date.today())
    summary = models.TextField(default="this is a product")



