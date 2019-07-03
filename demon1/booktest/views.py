from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from .models import *


def index(request):
     # return HttpResponse('首页' "<a href='/list/'>跳转列表</a>")
    # tem1=loader.get_template('booktest/index.html')
    # result=tem1.render({'username':'lty'})
    # return HttpResponse(result)

    return render(request,'booktest/index.html',{'username':'lty'})

def list(request):

    s="""
    <br/>
    <a href='/detail/1/'>跳转详情1</a>
    <br/>
    <a href='/detail/2/'>跳转详情2</a>
    <br/>
    <a href='/detail/3/'>跳转详情3</a>
    """

    # return HttpResponse('列表页 %s'%(s,))
    # tem2=loader.get_template('booktest/list.html')
    books=BookInfo.objects.all()
    # result=tem2.render({'books':books})
    # return HttpResponse(result)
    return render(request,'booktest/list.html',{'books':books})

def detail(request,id):
    # return HttpResponse('详情页%s' "<a href='/'>跳转首页</a>"%(id,))

    # tem3=loader.get_template('booktest/detail.html')
    book=BookInfo.objects.get(pk=id)
    # result=tem3.render({'book':book})
    # return HttpResponse(result)
    return render(request,'booktest/detail.html',{'book':book})