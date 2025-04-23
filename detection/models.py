from django.db import models

class Detection(models.Model):
    image = models.ImageField(upload_to='images/')
    prediction = models.JSONField()

    def __str__(self):
        return f"Detection {self.id}"
