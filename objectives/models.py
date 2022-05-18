from django.db import models

# Create your models here.

class Objective(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateTimeField(null=False)

    def __str__(self):
        return str(self.name)
