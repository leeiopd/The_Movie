from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    subscribers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='subscribe')
    
    def __str__(self):
        return f'{self.pk}: {self.username}'

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=30)
    introduction = models.TextField()
    point = models.IntegerField()
    