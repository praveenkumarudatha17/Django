from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# Create your models here.
class Employee(models.Model):
    ename=models.CharField(max_length=64)
    eno=models.IntegerField()
    esal=models.FloatField()
    eaddr=models.CharField(max_length=64)

# Automated token generation
@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None,created=False,**kwargs):
    if created:
        Token.objects.create(user=instance)