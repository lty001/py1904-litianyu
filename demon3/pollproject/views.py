from django.shortcuts import render,redirect,reverse
from .models import *
from django.http import HttpResponse
from django.contrib.auth import login as lon,logout as lot,authenticate
from .forms import *
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
    lgf = LoginForm()
    rgf = RegisterForm()
    if request.method=='GET':
        return render(request,'pollproject/login.html',{'lgf':lgf,'rgf':rgf})
    elif request.method=='POST':
        # response=redirect(reverse('pollproject:index'))
        # response.set_cookie('username',request.POST.get('username'))
        # return response
        # request.session['username']=request.POST.get('username')
        # return redirect(reverse('pollproject:index'))
        # username=request.POST.get('username')
        # password=request.POST.get('password')
        lgf=LoginForm(request.POST)
        if lgf.is_valid():
            username=lgf.cleaned_data['username']
            password=lgf.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            if user:
                lon(request,user)
                return redirect(reverse('pollproject:index'))
            else:
                return render(request,'pollproject/login.html',{'errors':'登录失败','lgf':lgf,'rgf':rgf})
        else:
            return render(request, 'pollproject/login.html', {'errors': '登录失败','lgf':lgf,'rgf':rgf})



def logout(request):
    # res=redirect(reverse('pollproject:login'))
    # res.delete_cookie('username')
    # return res
    # request.session.flush()
    lot(request)
    return redirect(reverse('pollproject:login'))

def regist(request):
    if request.method=='POST':
        rgf=RegisterForm(request.POST)
        if rgf.is_valid():
            user=rgf.save(commit=False)
            user.set_password(rgf.cleaned_data['password'])
            user.save()
            return redirect(reverse('pollproject:login'))
        else:
            lgf=LoginForm()
            rgf=RegisterForm()
            return render(request,'pollproject/login.html',{'errors':'注册失败','lgf':lgf,'rgf':rgf})
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

