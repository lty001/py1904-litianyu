from django.shortcuts import render,redirect,reverse

# Create your views here.

from .models import *
from django.views.generic import View,TemplateView,ListView



def index(request):

    questions=Question.objects.all()
    return render(request,'voteproject/index.html',locals())


def vote(request,id):

    question=Question.objects.get(pk=id)
    if request.method=='GET':
        return render(request, 'voteproject/vote.html', locals())
    elif request.method=='POST':
        choiceid=request.POST.get('choice')
        choice=Choice.objects.get(pk=choiceid)
        choice.votes +=1
        choice.save()
        return redirect(reverse('voteproject:result',args=(id,)))

def result(request,id):
    question = Question.objects.get(pk=id)
    return render(request,'voteproject/result.html',locals())