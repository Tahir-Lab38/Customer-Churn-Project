from django.db import models

# Create your models here.

class Customer(models.Model):
    feature1 = models.FloatField()
    feature2 = models.FloatField()
    # Add other features as necessary

    def __str__(self):
        return str(self.id)
