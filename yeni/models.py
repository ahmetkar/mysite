from django.db import models

# Create your models here.
class Tablo1(models.Model):
  sayi = models.IntegerField(default=0)
  date = models.DateTimeField('date published')