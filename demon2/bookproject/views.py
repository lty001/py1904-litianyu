from django.shortcuts import render,redirect,reverse
from .models import *
from django.http import HttpResponse
from django.template import loader

# Create your views here.



def index(request):
    # temp=loader.get_template('bookproject/index.html')
    # result=temp.render({'username':'lty'})
    # return HttpResponse(result)

    return render(request,'bookproject/index.html',{'username':'lty'})

def list(request):
    country=Country.objects.all()
    return render(request,'bookproject/list.html',locals())

def detail(request,id):
    ct=Country.objects.get(pk=id)
    return render(request,'bookproject/detail.html',locals())

def deletecountry(request,id):
    ct = Country.objects.get(pk=id)
    ct.delete()
    return redirect(reverse('bookproject:list'))

def deletehero(request,id):
    hero=Hero.objects.get(pk=id)
    ctid=hero.ctry.id
    hero.delete()
    return redirect(reverse('bookproject:detail',args=(ctid,)))

def addhero(request,id):
    ct=Country.objects.get(pk=id)
    if request.method=='GET':
        return render(request,'bookproject/addhero.html',{'ct':ct})
    elif request.method=='POST':
        name=request.POST.get('username')
        content=request.POST.get('content')
        gender=request.POST.get('gender')
        hero=Hero()
        hero.hname=name
        hero.content=content
        hero.gender=gender
        hero.ctry=ct
        hero.save()
        return redirect(reverse('bookproject:detail',args=(id,)))