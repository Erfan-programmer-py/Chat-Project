from django.db import models

# Create your models here.


class MessageModel(models.Model):
    message = models.TextField()
