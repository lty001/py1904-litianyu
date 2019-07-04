from django.db import models

# Create your models here.


class VoteTitle(models.Model):
    title=models.CharField(max_length=100)

    def __str__(self):
        return self.title

class VoteAnswer(models.Model):
    answer=models.CharField(max_length=20)
    num=models.IntegerField(max_length=10)
    link=models.ForeignKey(VoteTitle,on_delete=models.CASCADE)

    def __str__(self):
        return self.answer