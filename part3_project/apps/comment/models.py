from django.db import models
from fruitmall.models import *

# Create your models here.



class Comment(models.Model):
    name=models.CharField(max_length=10)
    content=models.TextField()
    create_time=models.DateTimeField(auto_now_add=True)
    goods=models.ForeignKey(AddGoods,on_delete=models.CASCADE)

    def __str__(self):
        return self.name