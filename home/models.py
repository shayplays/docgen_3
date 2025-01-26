from django.db import models

class LegalDocument(models.Model):
    DOCUMENT_CHOICES = [
        ('will', 'Simple Will'),
        ('license', 'License Agreement')
    ]
    document_type = models.CharField(max_length=10, choices=DOCUMENT_CHOICES)
    name = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    age = models.IntegerField(blank=True, null=True)
    address = models.TextField()
    executor_name = models.CharField(max_length=255, blank=True, null=True)
    wife_name = models.CharField(max_length=255, blank=True, null=True)
    child_name_1 = models.CharField(max_length=255, blank=True, null=True)
    child_name_2 = models.CharField(max_length=255, blank=True, null=True)
    flat_no = models.CharField(max_length=50, blank=True, null=True)
    flat_address = models.TextField(blank=True, null=True)
    date = models.CharField(max_length=50)
    month = models.CharField(max_length=50, blank=True, null=True)
    year = models.CharField(max_length=50, blank=True, null=True)
    time = models.CharField(max_length=50, blank=True, null=True)
    