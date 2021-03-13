from django.db import models

class JSONFile(models.Model):
    file = models.FileField()

class JsonDetails(models.Model):
    id = models.DecimalField(primary_key=True,max_digits=10, decimal_places=0, blank=False, null=False)
    userId = models.DecimalField(max_digits=10, decimal_places=0, blank=False, null=False)
    title = models.CharField(max_length=50)
    body = models.TextField(max_length=250)
