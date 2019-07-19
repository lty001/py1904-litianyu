from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Ads(models.Model):
    img=models.ImageField(upload_to='ads',verbose_name='图片')
    desc=models.CharField(max_length=10,verbose_name='简介')
    index=models.IntegerField(default=0,verbose_name='插入位置')

    def __str__(self):
        return self.desc

class UserAccount(models.Model):
    account=models.CharField(max_length=10,verbose_name='账号')
    password=models.CharField(max_length=20,verbose_name='密码')
    telephone=models.CharField(max_length=11,verbose_name='电话')
    email=models.EmailField(blank=True,null=True,verbose_name='邮箱')

    def __str__(self):
        return self.account

class UserPack(models.Model):
    address=models.CharField(max_length=50,verbose_name='地址')
    integral=models.IntegerField(default=0,verbose_name='积分')
    coupon=models.IntegerField(default=0,verbose_name='优惠券')
    account=models.ForeignKey(UserAccount,on_delete=models.CASCADE,verbose_name='账号')

    def __str__(self):
        return self.address

class Tags(models.Model):
    title=models.CharField(max_length=20,verbose_name='标签')

    def __str__(self):
        return self.title

class Category(models.Model):
    title=models.CharField(max_length=20,verbose_name='分类')

    def __str__(self):
        return self.title

class AddGoods(models.Model):
    name=models.CharField(max_length=10,verbose_name='商品名')
    img=models.ImageField(upload_to='goods',verbose_name='图片')
    desc=models.CharField(max_length=50,verbose_name='简介')
    price=models.CharField(max_length=10,verbose_name='价格')
    num=models.IntegerField(default=100,verbose_name='数量')
    wight=models.IntegerField(default=100,verbose_name='重量')
    integral=models.IntegerField(default=5,verbose_name='积分')
    update_time=models.DateTimeField(auto_now_add=True,verbose_name='时间')
    tags=models.ManyToManyField(Tags,verbose_name='标签')
    category=models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='分类')

    def __str__(self):
        return self.name

class GoodsDetail(models.Model):
    name=models.ForeignKey(AddGoods,on_delete=models.CASCADE,verbose_name='商品名')
    sales=models.IntegerField(default=0,verbose_name='销量')
    evaluate=models.IntegerField(default=0,verbose_name='累计评价')
    img=models.ImageField(upload_to='good',verbose_name='图片')
    body=models.TextField(verbose_name='内容')

    def __str__(self):
        return self.name

class Cart(models.Model):
    name=models.ForeignKey(AddGoods,on_delete=models.CASCADE,verbose_name='商品名')
    count=models.IntegerField(default=1,verbose_name='数量')

    def __str__(self):
        return self.name


class News(models.Model):
    title=models.CharField(max_length=20,verbose_name='标题')
    author=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='作者')
    views=models.IntegerField(default=0,verbose_name='浏览次数')
    body=models.TextField(verbose_name='内容')
    creatr_time=models.DateTimeField(auto_now_add=True,verbose_name='时间')

    def __str__(self):
        return self.title

