from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey, OneToOneField
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Agents(models.Model):
    user = OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    agent = ForeignKey(Agents, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name

