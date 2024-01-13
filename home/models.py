from django.db import models

# Create your models here.

class ContactMessage(models.Model):
    email = models.CharField(max_length=100)
    message=models.TextField()
    message_date = models.DateField(auto_now=True)
    message_replied = models.BooleanField(default=False)
    