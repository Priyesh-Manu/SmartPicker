from django.db import models

# Create your models here.

class ContactMessage:
    email = models.CharField(max_length=100)
    message=models.TextField()