from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4


class User(AbstractUser):
    # Using username, password, first_name, last_name, email from AbstractUser
    uuid = models.UUIDField(primary_key=True, default=uuid4, unique=True)


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=5000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
