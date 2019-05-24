from django.db import models

# Create your models here.
class ContactData(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    loc=models.CharField(max_length=50)
    number=models.BigIntegerField()
    sal=models.IntegerField()