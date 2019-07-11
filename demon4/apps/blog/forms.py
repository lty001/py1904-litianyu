from django import forms
from .models import Article
from comment.models import Comment



class ArticleForm(forms.ModelForm):
    class Meta:
        model=Article
        fields=['title','body','tags','category']
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'输入标题'}),

        }
        labels={
            'title':'文章标题',
            'body':'文章内容',
            'tags':'标签',
            'category':'分类'
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['name','email','url','content']