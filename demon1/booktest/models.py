from django.db import models
# from django.contrib.auth.models import User

# Create your models here.

class BookInfo(models.Model):
    title=models.CharField(max_length=20)
    pub_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class HeroInfo(models.Model):
    name=models.CharField(max_length=20)
    # gender=models.BooleanField(default=True)
    gender=models.CharField(max_length=5,choices=(('man','男'),('woman','女')))
    camp=models.CharField(max_length=5,choices=(('good','光明'),('bad','黑暗')),default='good')
    content=models.CharField(max_length=100)
    book=models.ForeignKey(BookInfo,on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class User(models.Model):
    name=models.CharField(max_length=10)

class Tel(models.Model):
    num=models.CharField(max_length=11)
    username=models.ForeignKey(User,on_delete=models.CASCADE)


class Account(models.Model):
    username=models.CharField(max_length=10)

class Password(models.Model):
    pwd=models.CharField(max_length=10)
    acc=models.OneToOneField(Account,on_delete=models.CASCADE)


class Host(models.Model):
    hname=models.CharField(max_length=10)

class App(models.Model):
    aname=models.CharField(max_length=10)
    h=models.ManyToManyField(Host)

