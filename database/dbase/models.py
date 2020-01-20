from django.db import models

# Create your models here.

class user(models.Model):
    u_name = models.CharField(max_length = 248)
    email = models.CharField(max_length = 248)
