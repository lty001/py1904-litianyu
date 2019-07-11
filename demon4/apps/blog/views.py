from django.shortcuts import render,redirect,reverse
from .models import *
from django.http import HttpResponse
from django.views import View
from .forms import ArticleForm
from django.core.paginator import Paginator,Page

# Create your views here.


class IndexView(View):
    def get(self,request):
        ads=Ads.objects.all()
        articles=Article.objects.all()

        pagenum=request.GET.get('page')
        pagenum = 1 if not pagenum else pagenum
        page=Paginator(articles,2).get_page(pagenum)


        return render(request,'blog/index.html',locals())


class SingleView(View):
    def get(self,request,id):
        article=Article.objects.all()
        return render(request,'blog/single.html',locals())

    def post(self,request,id):
        return HttpResponse('评论')


class AddArticleView(View):
    def get(self,request):
        af=ArticleForm()
        return render(request,'blog/addarticle.html',locals())

    def post(self,request):
        af=ArticleForm(request.POST)
        if af.is_valid():
            article=af.save(commit=False)
            article.category=Category.objects.first()
            print(Category.objects.first().title)
            article.author=User.objects.first()
            article.save()
            return redirect(reverse('blog:index'))
        else:
            return HttpResponse('添加失败')