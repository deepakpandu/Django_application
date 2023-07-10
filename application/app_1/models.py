from django.db import models

# Create your models here.

class tech(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  address = models.CharField(null=True, max_length=255)
