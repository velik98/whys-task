
from django.db import models

class ModelData(models.Model):
    model_name = models.CharField(max_length=255)
    data = models.JSONField()

    def __str__(self):
        return f"{self.model_name} - {self.column1}"
