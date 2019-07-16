from django.conf.urls import url
from . import views




app_name='fruitmall'

urlpatterns=[
    url(r'^$', views.IndexView.as_view(), name='index'),              #首页
    url(r'^regist/$', views.RegistView.as_view(), name='regist'),     #注册
    url(r'^login/$', views.LoginView.as_view(), name='login'),        #登录
    url(r'^information/$', views.InformationView.as_view(), name='information'),  #资讯信息
    url(r'^information01/$', views.Information01View.as_view(), name='information01'),  #资讯详情
    url(r'^product/$', views.ProductView.as_view(), name='product'),              #产品分类
    url(r'^details/$', views.DetailsView.as_view(), name='details'),              #产品详情
    url(r'^record/$', views.RecordView.as_view(), name='record'),                 #个人信息
    url(r'^address/$', views.AddressView.as_view(), name='address'),              #收货地址
    url(r'^coupon/$', views.CouponView.as_view(), name='coupon'),                 #优惠券
    url(r'^integral/$', views.IntegralView.as_view(), name='integral'),           #积分
    url(r'^data/$', views.DataView.as_view(), name='data'),                       #修改资料
    url(r'^cart/$', views.CartView.as_view(), name='cart'),                       #购物车
    url(r'^settlement/$', views.SettlementView.as_view(), name='settlement'),     #立刻购买
    url(r'^pay/$', views.PayView.as_view(), name='pay'),                          #支付
    url(r'^contact/$', views.ContactView.as_view(), name='contact'),              #联系
]