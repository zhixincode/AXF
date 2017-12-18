from django.conf.urls import url

from App import views

urlpatterns = [
    url(r'home/', views.Home, name='home'),
    url(r'market/', views.Market, name='market'),
    url(r'cart/', views.Cart, name='cart'),
    url(r'mine/', views.Mine, name='mine'),
    url(r'marketcategory/(\d+)/(\d+)/(\d+)', views.MarketCategory, name='marketcategory'),
    url(r'^register/', views.register, name='register'),
    # 验证账号是否被注册
    url(r'^checkuserid/$', views.checkuserid, name="checkuserid"),
    # url(r'^cart/$', views.cart, name="cart"),
    # 修改购物车
    url(r'^changecart/(\d+)/$', views.changecart, name="changecart"),
    # 下订单
    # url(r'^saveorder/$', views.saveorder, name="saveorder"),
    url(r'^jumptwo/',views.jumpTwo,name="jumptwo"),
    #登录url
    url(r'^login/$',views.Login,name='login'),
    # ajax登录校验url
    url(r'^logincheck/$', views.loginCheck,name='logincheck'),
    url(r'^quit/$', views.quit),

]
