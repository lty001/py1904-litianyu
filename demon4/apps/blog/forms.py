from django import forms
from .models import Article



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