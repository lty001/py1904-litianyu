from . import views
from django.conf.urls import url


app_name='pollproject'

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^list/(\d+)/$',views.list,name='list'),
    url(r'^detail/(\d+)/$',views.detail,name='detail'),
]