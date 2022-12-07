from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class ResumeModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField("имя", max_length=50)
    surname = models.CharField("фамилия", max_length=50)
    age = models.IntegerField("возраст")
    company = models.CharField("предыдущее место работы", max_length=50)
    position = models.CharField("должность", max_length=50)
    experience = models.IntegerField("стаж")