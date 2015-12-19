from django.db import models

# Create your models here.
class AWSTestModel(models.Model):
    random_text = models.CharField(max_length=200)
    new_field = models.CharField(max_length=600, default="some more data")
