from django.shortcuts import render,redirect,reverse,get_object_or_404,get_list_or_404
from django.contrib.auth import login,logout,authenticate
from django.views import View
from .models import *
from comment.models import *
from .forms import *
from django.core.paginator import Paginator




# Create your views here.



#分页函数
def getpage(request,object_list,per_num):
    pagenum = request.GET.get('page')
    pagenum = 1 if not pagenum else pagenum
    page = Paginator(object_list, per_num).get_page(pagenum)
    return page



#注册
class RegistView(View):
    def get(self,request):
        return render(request,'fruitmall/regist.html')

    def post(self,request):
        rgf=RegistForm(request.POST)
        account=request.POST.get('account')
        ua=UserAccount.objects.all().filter(account=account).first()
        if ua==None:
            if rgf.is_valid():
                user=rgf.save(commit=False)
                user.save()
                return redirect(reverse('fruitmall:login'))
            else:
                lgf=LoginForm()
                rgf=RegistForm()
                return render(request,'fruitmall/regist.html',{'error':'注册失败','lgf':lgf,'rgf':rgf})
        else:
            return render(request,'fruitmall/regist.html')

#登录
class LoginView(View):
    def get(self,request):
        rgf = RegistForm
        lgf = LoginForm
        return render(request,'fruitmall/login.html',locals())

    def post(self,request):
        lgf=LoginForm(request.POST)
        if lgf.is_valid():
            account=lgf.cleaned_data['account']
            password=lgf.cleaned_data['password']
            user=UserAccount.objects.all().filter(account=account,password=password).first()
            if user:
                response = redirect(reverse('fruitmall:index'))
                response.set_cookie('account', account)
                return response
            else:
                return render(request,'fruitmall/login.html',{'lgf':lgf})
        else:
            return render(request,'fruitmall/login.html',{'lgf':lgf})

#首页
class IndexView(View):
    def get(self,request):
        ads=Ads.objects.all()
        account = request.COOKIES.get('account')
        goods = AddGoods.objects.all()
        return render(request,'fruitmall/index.html',locals())


#资讯
class InformationView(View):
    def get(self,request):
        ads = Ads.objects.all()
        account = request.COOKIES.get('account')
        goods = AddGoods.objects.all()
        news=News.objects.all()
        page=getpage(request,news,2)
        return render(request,'fruitmall/information.html',locals())

#资讯详情
class Information01View(View):
    def get(self,request,id):
        ads = Ads.objects.all()
        account = request.COOKIES.get('account')
        goods = AddGoods.objects.all()
        news = get_list_or_404(News,pk=id)
        return render(request,'fruitmall/information01.html',locals())

    def post(self,request,id):
        news=get_object_or_404(News,pk=id)
        return redirect(reverse('fruitmall:information01',args=(news.id)),locals())

#分类
class ProductView(View):
    def get(self,request):
        ads = Ads.objects.all()
        account = request.COOKIES.get('account')
        goods = AddGoods.objects.all()
        page = getpage(request, goods, 4)
        return render(request,'fruitmall/product.html',locals())

#商品详情
class DetailsView(View):
    def get(self,request,id):
        account = request.COOKIES.get('account')
        comment = Comment.objects.all()
        gd=GoodsDetail.objects.all()
        goods = get_list_or_404(AddGoods,pk=id)
        page=getpage(request,comment,4)
        return render(request,'fruitmall/details.html',locals())

    def post(self,request,id):
        goods=get_object_or_404(AddGoods,pk=id)
        gdetail=GoodsDetail.objects.all()
        return redirect(reverse('fruitmall:details',args=(goods.id)),locals())

#个人
class RecordView(View):
    def get(self,request):
        account = request.COOKIES.get('account')
        up=UserPack.objects.all()
        goods = AddGoods.objects.all()
        cart=Cart.objects.all()
        page=getpage(request,goods,3)
        return render(request,'fruitmall/record.html',locals())

#修改信息
class DataView(View):
    def get(self,request):
        up = UserPack.objects.all()
        account = request.COOKIES.get('account')
        goods = AddGoods.objects.all()
        return render(request,'fruitmall/data.html',locals())

#地址管理
class AddressView(View):
    def get(self,request):
        up = UserPack.objects.all()
        account = request.COOKIES.get('account')
        return render(request,'fruitmall/address.html',locals())

#优惠券
class CouponView(View):
    def get(self,request):
        up = UserPack.objects.all()
        account = request.COOKIES.get('account')
        goods = AddGoods.objects.all()
        page=getpage(request,goods,4)
        return render(request,'fruitmall/coupon.html',locals())

#积分
class IntegralView(View):
    def get(self,request):
        up = UserPack.objects.all()
        account = request.COOKIES.get('account')
        goods = AddGoods.objects.all()
        page=getpage(request,goods,4)
        return render(request,'fruitmall/integral.html',locals())

#购物车
class CartView(View):
    def get(self,request):
        account = request.COOKIES.get('account')
        goods = AddGoods.objects.all()
        page=getpage(request,goods,2)
        return render(request,'fruitmall/cart.html',locals())

#去购买
class SettlementView(View):
    def get(self,request):
        account = request.COOKIES.get('account')
        goods = AddGoods.objects.all()
        page=getpage(request,goods,2)
        return render(request,'fruitmall/settlement.html',locals())

#付款
class PayView(View):
    def get(self,request):
        account = request.COOKIES.get('account')
        goods = AddGoods.objects.all()
        return render(request,'fruitmall/pay.html',locals())

#联系
class ContactView(View):
    def get(self,request):
        ads = Ads.objects.all()
        account = request.COOKIES.get('account')
        goods = AddGoods.objects.all()
        return render(request,'fruitmall/contact.html',locals())


class LogoutView(View):
    def get(self,request):
        response = redirect(reverse('fruitmall:login'))
        response.delete_cookie('account')
        return response