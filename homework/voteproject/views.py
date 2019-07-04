from django.shortcuts import render,redirect,reverse

# Create your views here.

from .models import *
from django.views.generic import View,TemplateView,ListView



def index(request):

    title=VoteTitle.objects.all()
    return render(request,'voteproject/index.html',{'titles':title})


def vote(request,id):
    link=VoteTitle.objects.get(pk=id)
    return render(request, 'voteproject/vote.html', {'link': link})


def result(request):
    ret=VoteAnswer.objects.all()
    return render(request,'voteproject/result.html',{'result':ret})