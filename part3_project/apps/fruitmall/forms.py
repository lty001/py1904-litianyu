from django import forms
from .models import *




class LoginForm(forms.ModelForm):
    class Meta:
        model=UserAccount
        fields=['account','password']
        widgets={
            'account': forms.TextInput(attrs={'id': 'username', 'placeholder': '输入用户名', 'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'id': 'password', 'placeholder': '输入密码', 'class': 'form-control'}),
        }
        help_texts={
            'account':''
        }


class RegistForm(forms.ModelForm):
    repeatpassword = forms.CharField(label='确认密码', max_length=10, required=True, widget=forms.PasswordInput(
        attrs={'id': 'repeatpassword', 'placeholder': '确认密码', 'class': 'form-control'}))
    class Meta:
        model=UserAccount
        fields=['account','password','telephone','email']
        widgets={
            'account': forms.TextInput(attrs={'id': 'registusername', 'placeholder': '输入用户名', 'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'id': 'registpassword', 'placeholder': '输入密码', 'class': 'form-control'}),
            'telephone': forms.TextInput(attrs={'id': 'telephoe', 'placeholder': '输入手机号', 'class': 'form-control'}),
            'email': forms.TextInput(attrs={'id': 'email', 'placeholder': '输入邮箱', 'class': 'form-control'}),
        }
        help_texts={
            'account':''
        }
        labels={
            'account':'输入用户名',
            'password':'输入密码',
            'telephone':'输入手机号',
            'email':'输入邮箱'
        }