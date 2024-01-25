from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class User(User):
    pass


class Data(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True, related_name="user"
    )
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    phone = models.IntegerField(max_length=255)
    email = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    created = models.DateField(auto_now_add=True)
