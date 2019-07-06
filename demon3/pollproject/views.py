from django.shortcuts import render,redirect,reverse
from .models import *
from django.http import HttpResponse
# Create your views here.



def index(request):
    questions=Question.objects.all()
    return render(request,'pollproject/index.html',locals())

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


def detail(request,id):
    question=Question.objects.get(pk=id)
    return render(request,'pollproject/detail.html',locals())

