from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Ads(models.Model):
    img=models.ImageField(upload_to='ads')
    desc=models.CharField(max_length=10)
    index=models.IntegerField(default=0)

class UserAccount(models.Model):
    account=models.CharField(max_length=10)
    password=models.CharField(max_length=20)
    telephone=models.CharField(max_length=11)
    email=models.EmailField(blank=True,null=True)

class UserPack(models.Model):
    address=models.CharField(max_length=50)
    integral=models.IntegerField(default=0)
    coupon=models.IntegerField(default=0)
    account=models.ForeignKey(UserAccount,on_delete=models.CASCADE)

class Tags(models.Model):
    title=models.CharField(max_length=20)

class Category(models.Model):
    title=models.CharField(max_length=20)

class AddGoods(models.Model):
    name=models.CharField(max_length=10)
    img=models.ImageField(upload_to='goods')
    desc=models.CharField(max_length=50)
    price=models.CharField(max_length=10)
    num=models.IntegerField(default=100)
    wight=models.IntegerField(default=100)
    integral=models.IntegerField(default=5)
    update_time=models.DateTimeField(auto_now_add=True)
    tags=models.ManyToManyField(Tags)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

class GoodsDetail(models.Model):
    name=models.ForeignKey(AddGoods,on_delete=models.CASCADE)
    sales=models.IntegerField(default=0)
    evaluate=models.IntegerField(default=0)
    img=models.ImageField(upload_to='good')
    body=models.TextField()

class Cart(models.Model):
    name=models.ForeignKey(AddGoods,on_delete=models.CASCADE)
    count=models.IntegerField(default=1)


class News(models.Model):
    title=models.CharField(max_length=20)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    views=models.IntegerField(default=0)
    body=models.TextField()
    creatr_time=models.DateTimeField(auto_now_add=True)

