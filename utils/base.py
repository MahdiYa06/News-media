from django.db import models


class TimeStampModel(models.Model):
    created_at = models.DateTimeField('Creatd_at', auto_now_add=True)
    created_at = models.DateTimeField('Updated_at', auto_now=True)
    
    class Meta:
        abstract = True