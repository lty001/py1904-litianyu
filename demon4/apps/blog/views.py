from django.shortcuts import render,redirect,reverse,get_object_or_404
from .models import *
from django.http import HttpResponse
from django.views import View
from .forms import ArticleForm,CommentForm
from django.core.paginator import Paginator,Page

# Create your views here.


def getpage(request,object_list,per_num):
    pagenum = request.GET.get('page')
    pagenum = 1 if not pagenum else pagenum
    page = Paginator(object_list, per_num).get_page(pagenum)
    return page


class IndexView(View):
    def get(self,request):
        ads=Ads.objects.all()
        articles=Article.objects.all()
        page=getpage(request,articles,2)
        return render(request,'blog/index.html',locals())


class SingleView(View):
    def get(self,request,id):
        article=get_object_or_404(Article,pk=id)
        article.views+=1
        article.save()
        cf=CommentForm()
        return render(request,'blog/single.html',{'article':article,'cf':cf})

    def post(self,request,id):
        article = get_object_or_404(Article, pk=id)
        cf=CommentForm(request.POST)
        comment=cf.save(commit=False)
        comment.article=article
        comment.save()
        return redirect(reverse('blog:single',args=(article.id,)))


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

class ContactView(View):
    def get(self,request):
        return render(request,'blog/contact.html')


class ArchivesView(View):
    def get(self,request,year,month):
        ads = Ads.objects.all()
        article=Article.objects.filter(create_time__year=year,create_time__month=month)
        page = getpage(request, article, 1)
        return render(request,'blog/index.html',{'article':article,'ads':ads,'page':page})


class CategoryView(View):
    def get(self,request,id):
        ads=Ads.objects.all()
        article=Article.objects.filter(category=Category.objects.get(pk=id))
        page = getpage(request, article, 2)
        return render(request,'blog/index.html',locals())


class TagsView(View):
    def get(self,request,id):
        ads = Ads.objects.all()
        article = Article.objects.filter(tags=Tag.objects.get(pk=id))
        page = getpage(request, article, 2)
        return render(request, 'blog/index.html',locals())