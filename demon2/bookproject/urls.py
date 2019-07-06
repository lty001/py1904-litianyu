from .models import *
from . import views
from django.conf.urls import url



app_name='bookproject'

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^list/$',views.list,name='list'),
    url(r'^detail/(\d+)/$',views.detail,name='detail'),
    url(r'^deletecountry/(\d+)/$',views.deletecountry,name='deletecountry'),
    url(r'^deletehero/(\d+)/$',views.deletehero,name='deletehero'),
    url(r'^addhero/(\d+)/$',views.addhero,name='addhero'),
    url(r'^addcountry/$',views.addcountry,name='addcountry')
]