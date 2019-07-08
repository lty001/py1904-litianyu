from django.shortcuts import render,redirect,reverse
from .models import *
from django.http import HttpResponse
from django.contrib.auth import login as lon,logout as lot,authenticate
# Create your views here.


def checklogin(fun):
    def check(request,*args):
        # username=request.COOKIES.get('username')
        # username = request.session.get('username')
        if request.user and request.user.is_authenticated:
            return fun(request,*args)
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
def list(request,id):
    question=Question.objects.get(pk=id)
    if request.method=='GET':
        return render(request,'pollproject/list.html',locals())
    elif request.method=='POST':
        choiceid=request.POST.get('choice')
        choice=Choice.objects.get(pk=choiceid)
        choice.votes+=1
        choice.save()
        return redirect(reverse('pollproject:detail',args=(id,)),locals())


@checklogin
def detail(request,id):
    question=Question.objects.get(pk=id)
    return render(request,'pollproject/detail.html',locals())

def login(request):
    if request.method=='GET':
        return render(request,'pollproject/login.html')
    elif request.method=='POST':
        # response=redirect(reverse('pollproject:index'))
        # response.set_cookie('username',request.POST.get('username'))
        # return response
        # request.session['username']=request.POST.get('username')
        # return redirect(reverse('pollproject:index'))
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user:
            lon(request,user)
            return redirect(reverse('pollproject:index'))
        else:
            return render(request,'pollproject/login.html',{'errors':'登录失败'})



def logout(request):
    # res=redirect(reverse('pollproject:login'))
    # res.delete_cookie('username')
    # return res
    # request.session.flush()
    lot(request)
    return redirect(reverse('pollproject:login'))

def regist(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        try:
            user=PollUser.objects.create_user(username=username,password=password)
        except:
            user=None
        if user:
            return redirect(reverse('pollproject:login'))
        else:
            return render(request,'pollproject/login.html',{'errors':'注册失败'})

