
from django.conf.urls import url
from . import views
app_name='booktest'

urlpatterns=[
    # url(r'^$',views.index,name='index'),
    # url(r'^$',views.IndexView.as_view(),name='index'),
    url(r'^$',views.IndexTemplateView.as_view(),name='index'),
    url(r'^list/$',views.list,name='list'),
    url(r'^detail/(\d+)/$',views.detail,name='detail'),
    url(r'^deleteHero/(\d+)/$',views.deleteHero,name='deleteHero'),
    url(r'^addHero/(\d+)/$',views.addHero,name='addHero'),
    url(r'^deleteBook/(\d+)/$',views.deleteBook,name='deleteBook'),
]