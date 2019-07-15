from django.shortcuts import render, redirect, reverse
from .models import *
from django.http import HttpResponse
from django.contrib.auth import login as lon, logout as lot, authenticate
from .forms import *
from PIL import Image,ImageDraw,ImageFont
import random,io
from django.core.cache import cache
from django.core.mail import send_mail,EmailMultiAlternatives
from django.conf import settings
from itsdangerous import TimedJSONWebSignatureSerializer

# Create your views here.


def checklogin(fun):
    def check(request, *args):
        # username=request.COOKIES.get('username')
        # username = request.session.get('username')
        if request.user and request.user.is_authenticated:
            return fun(request, *args)
        else:
            return redirect(reverse('pollproject:login'))

    return check


@checklogin
def index(request):
    # username = request.COOKIES.get('username')
    # username = request.session.get('username')
    questions = Question.objects.all()
    return render(request, 'pollproject/index.html', locals())

    # username=request.COOKIES.get('username')
    # if username:
    #     questions=Question.objects.all()
    #     return render(request,'pollproject/index.html',locals())
    # else:
    #     return redirect(reverse('pollproject:login'))


@checklogin
def list(request, id):
    question = Question.objects.get(pk=id)
    if request.method == 'GET':
        return render(request, 'pollproject/list.html', locals())
    elif request.method == 'POST':
        choiceid = request.POST.get('choice')
        choice = Choice.objects.get(pk=choiceid)
        choice.votes += 1
        choice.save()
        return redirect(reverse('pollproject:detail', args=(id,)), locals())


@checklogin
def detail(request, id):
    question = Question.objects.get(pk=id)
    return render(request, 'pollproject/detail.html', locals())


def login(request):
    lgf = LoginForm()
    rgf = RegisterForm()
    if request.method == 'GET':
        return render(request, 'pollproject/login.html', {'lgf': lgf, 'rgf': rgf})
    elif request.method == 'POST':
        # response=redirect(reverse('pollproject:index'))
        # response.set_cookie('username',request.POST.get('username'))
        # return response
        # request.session['username']=request.POST.get('username')
        # return redirect(reverse('pollproject:index'))
        # username=request.POST.get('username')
        # password=request.POST.get('password')

        verifycode=request.POST.get('verify')
        if not verifycode==cache.get('verify'):  #获取验证码缓存
            return HttpResponse('验证码错误')

        lgf = LoginForm(request.POST)
        if lgf.is_valid():
            username = lgf.cleaned_data['username']
            password = lgf.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                lon(request, user)
                return redirect(reverse('pollproject:index'))
            else:
                return render(request, 'pollproject/login.html', {'errors': '登录失败', 'lgf': lgf, 'rgf': rgf})
        else:
            return render(request, 'pollproject/login.html', {'errors': '登录失败', 'lgf': lgf, 'rgf': rgf})


def logout(request):
    # res=redirect(reverse('pollproject:login'))
    # res.delete_cookie('username')
    # return res
    # request.session.flush()
    lot(request)
    return redirect(reverse('pollproject:login'))


def regist(request):
    if request.method == 'POST':
        rgf = RegisterForm(request.POST)
        if rgf.is_valid():
            user = rgf.save(commit=False)
            user.set_password(rgf.cleaned_data['password'])
            user.save()
            return redirect(reverse('pollproject:login'))
        else:
            lgf = LoginForm()
            rgf = RegisterForm()
            return render(request, 'pollproject/login.html', {'errors': '注册失败', 'lgf': lgf, 'rgf': rgf})
        # username=request.POST.get('username')
        # password=request.POST.get('password')
        # try:
        #     user=PollUser.objects.create_user(username=username,password=password)
        # except:
        #     user=None
        # if user:
        #     return redirect(reverse('pollproject:login'))
        # else:
        #     return render(request,'pollproject/login.html',{'errors':'注册失败'})


def verify(request):


# 定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100),
               random.randrange(20, 100),
               random.randrange(20, 100))
    width = 100
    heigth = 25
    # 创建画面对象
    im = Image.new('RGB', (width, heigth), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, heigth))
    fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
    draw.point(xy, fill=fill)
    # 定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    print('当前验证码：',rand_str)
    #设置缓存验证码
    cache.set('verify',rand_str)
    # 构造字体对象
    font = ImageFont.truetype('FREESCPT.TTF', 23)
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    # 释放画笔
    del draw
    request.session['verifycode'] = rand_str
    f = io.BytesIO()
    im.save(f, 'png')
    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(f.getvalue(), 'image/png')
