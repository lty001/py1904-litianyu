from django import forms
from .models import PollUser


class LoginForm(forms.Form):
    username=forms.CharField(label='用户名',max_length=10,required=True,widget=forms.TextInput(attrs={'id':'username','class':'form-control','placeholder':'输入用户名'}))
    password=forms.CharField(label='密码',max_length=10,required=True,widget=forms.PasswordInput(attrs={'id':'username','class':'form-control','placeholder':'输入密码'}))


class RegisterForm(forms.ModelForm):
    repeatpassword=forms.CharField(label='确认密码',max_length=10,required=True,widget=forms.PasswordInput(attrs={'id':'repeatpassword','placeholder':'确认密码','class':'form-control'}))
    class Meta:
        model=PollUser
        fields=['username','password','telephone']
        widgets={
            'username':forms.TextInput(attrs={'id':'registusername','placeholder':'输入用户名','class':'form-control'}),
            'password':forms.PasswordInput(attrs={'id':'registpassword','placeholder':'输入密码','class':'form-control'}),
            'telephone':forms.TextInput(attrs={'id':'telephoe','placeholder':'输入手机号','class':'form-control'}),
        }
        help_texts={
            'username':''
        }
        labels={
            'telephone':'手机号'
        }