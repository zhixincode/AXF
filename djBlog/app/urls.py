from django.conf.urls import url

from app import views

urlpatterns = [
    url(r'^blog/',views.base,name='blog'),
    url(r'^success/$',views.success,name='success'),
    url(r'^show/$',views.showarticle,name='show'),
]