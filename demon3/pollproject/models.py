from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Question(models.Model):
    title=models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Choice(models.Model):
    desc=models.CharField(max_length=10)
    votes=models.IntegerField(default=0)
    question=models.ForeignKey(Question,on_delete=models.CASCADE)

    def __str__(self):
        return self.desc


class PollUser(User):
    telephone=models.CharField(max_length=11)