from django.db import models

class CbvModel(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    score = models.IntegerField()
