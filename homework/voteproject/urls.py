

from django.conf.urls import url
from . import views
app_name='voteproject'

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^vote/(\d+)/$',views.vote,name='vote'),
    url(r'^result/$',views.result,name='resule'),
]