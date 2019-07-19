import xadmin
from .models import *



class AdsAdminx(object):
    list_display=['img','desc','index']

class AddGoodsAdminx(object):
    list_display=['name','img','desc','price','num','wight','integral',
                  'update_time','tags','category']

class UserPackAdminx(object):
    list_display=['address','integral','coupon','account']

class UserAccountAdminx(object):
    list_display=['account','password','telephone','email']

class CartAdminx(object):
    list_display=['name','count']

class GoodsDetailAdminx(object):
    list_display=['name','sales','evaluate','img','body']

class NewsAdminx(object):
    list_display=['title','author','views','body','creatr_time']

class TagsAdmin(object):
    list_display=['title']

class CategoryAdmins(object):
    list_display=['title']

xadmin.site.register(Ads,AdsAdminx)
xadmin.site.register(AddGoods,AddGoodsAdminx)
xadmin.site.register(UserPack,UserPackAdminx)
xadmin.site.register(UserAccount,UserAccountAdminx)
xadmin.site.register(Tags,TagsAdmin)
xadmin.site.register(Category,CategoryAdmins)
xadmin.site.register(Cart,CartAdminx)
xadmin.site.register(GoodsDetail,GoodsDetailAdminx)
xadmin.site.register(News,NewsAdminx)
