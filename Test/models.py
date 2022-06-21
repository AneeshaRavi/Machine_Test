from django.db import models
from django.db import models
# Create your models here.
class Strings(models.Model):
    Master_String=models.CharField(max_length=50)
    String1=models.CharField(max_length=50)
    String2=models.CharField(max_length=50)
    String3=models.CharField(max_length=50)
    String4=models.CharField(max_length=50)