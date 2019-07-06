from django.db import models

# Create your models here.


class Country(models.Model):
    cname=models.CharField(max_length=10)

    def __str__(self):
        return self.cname

class Hero(models.Model):
    hname=models.CharField(max_length=10)
    gender=models.CharField(max_length=10,choices=(('男','男'),('女','女')))
    content=models.CharField(max_length=20)
    ctry=models.ForeignKey(Country,on_delete=models.CASCADE)

    def __str__(self):
        return self.hname
