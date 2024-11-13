from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
	ACCOUNT_TYPE_CHOICES = [
        ('user', 'User'),
        ('business', 'Business'),
        
    ]
	account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPE_CHOICES, default='user')




