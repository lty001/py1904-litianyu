from django.shortcuts import render,redirect,reverse
from django.views import View
from django.http import HttpResponse




# Create your views here.



class RegistView(View):
    def get(self,request):
        return render(request,'fruitmall/regist.html')

class LoginView(View):
    def get(self,request):
        return render(request,'fruitmall/login.html')


class IndexView(View):
    def get(self,request):
        return render(request,'fruitmall/index.html')

class InformationView(View):
    def get(self,request):
        return render(request,'fruitmall/information.html')

class Information01View(View):
    def get(self,request):
        return render(request,'fruitmall/information01.html')

class ProductView(View):
    def get(self,request):
        return render(request,'fruitmall/product.html')

class DetailsView(View):
    def get(self,request):
        return render(request,'fruitmall/details.html')

class RecordView(View):
    def get(self,request):
        return render(request,'fruitmall/record.html')

class DataView(View):
    def get(self,request):
        return render(request,'fruitmall/data.html')

class AddressView(View):
    def get(self,request):
        return render(request,'fruitmall/address.html')

class CouponView(View):
    def get(self,request):
        return render(request,'fruitmall/coupon.html')

class IntegralView(View):
    def get(self,request):
        return render(request,'fruitmall/integral.html')

class CartView(View):
    def get(self,request):
        return render(request,'fruitmall/cart.html')

class SettlementView(View):
    def get(self,request):
        return render(request,'fruitmall/settlement.html')

class PayView(View):
    def get(self,request):
        return render(request,'fruitmall/pay.html')

class ContactView(View):
    def get(self,request):
        return render(request,'fruitmall/contact.html')

