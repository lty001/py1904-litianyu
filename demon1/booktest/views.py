from django.shortcuts import render,redirect,reverse

# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import *
from django.views.generic import View,TemplateView,ListView


# class IndexView(View):
#     def get(self,request):
#         return render(request, 'booktest/index.html', {'username': 'lty'})

class IndexTemplateView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'booktest/index.html', {'username': 'lty'})

def index(request):

     # return HttpResponse('首页' "<a href='/list/'>跳转列表</a>")
    # tem1=loader.get_template('booktest/index.html')
    # result=tem1.render({'username':'lty'})
    # return HttpResponse(result)
    return render(request,'booktest/index.html',{'username':'lty'})


def list(request):

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

def deleteHero(request,id):
    hero=HeroInfo.objects.get(pk=id)
    bookid=hero.book.id
    hero.delete()
    # return HttpResponse('删除成功')
    # return HttpResponseRedirect('/detail/'+str(bookid)+'/')
    # return redirect('/detail/'+str(bookid)+'/')
    return redirect(reverse('booktest:detail',args=(bookid,)))

def addHero(request,id):

    book = BookInfo.objects.get(pk=id)
    if request.method=='GET':
        return render(request,'booktest/addHero.html',{'book':book})
    elif request.method=='POST':
        name=request.POST.get('username')
        content=request.POST.get('content')
        gender=request.POST.get('gender')
        camp=request.POST.get('camp')
        hero=HeroInfo()
        hero.name=name
        hero.content=content
        hero.book=book
        hero.gender=gender
        hero.camp=camp
        hero.save()
        return redirect(reverse('booktest:detail',args=(id,)))

def deleteBook(request,id):
    book=BookInfo.objects.get(pk=id)
    book.delete()
    return redirect(reverse('booktest:list'))