from django.db import models

# Create your models here.
class WillDocument(models.Model):
    name = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    age = models.IntegerField()
    address = models.TextField()
    executor_name = models.CharField(max_length=255)
    wife_name = models.CharField(max_length=255)
    child_name_1 = models.CharField(max_length=255)
    child_name_2 = models.CharField(max_length=255)
    flat_no = models.CharField(max_length=50)
    flat_address = models.TextField()
    date = models.CharField(max_length=50)
    month = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
    time = models.CharField(max_length=50)