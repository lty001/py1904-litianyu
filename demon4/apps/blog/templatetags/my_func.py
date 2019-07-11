from django.template import library



register=library.Library()

from blog.models import Article,Category,Tag

@register.simple_tag
def getlatestarticles(num=3):
    return Article.objects.order_by('-create_time')[:num]

@register.simple_tag
def gettimes(num=3):
    return Article.objects.dates('create_time','month','DESC')

@register.simple_tag
def getallcategorys(num=3):
    return Category.objects.order_by('title')[:num]

@register.simple_tag
def getalltags(num=3):
    return Tag.objects.order_by('title')[:num]

