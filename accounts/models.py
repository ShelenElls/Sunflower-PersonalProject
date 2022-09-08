from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    email = models.EmailField(unique=True)
    picture_url = models.URLField(null=True)

    def __str__(self):
        return f"{self.username}"