import time
import random
import os
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from AXF import settings
from App.models import Wheel, Nav, Shop, FoodTypes, MustBuy, MainShow, Goods, Register, User
import re
from .login.login import LoginForm
from django.http import HttpResponse


def Home(request):
    # 首页轮播
    wheelList = Wheel.objects.all()
    # 首页导航
    navList = Nav.objects.all()
    # 首页必买
    mustBuyList = MustBuy.objects.all()
    # 商店信息
    shopList = Shop.objects.all()
    mainshowList = MainShow.objects.all()
    shop1 = shopList[0:1]
    shop2 = shopList[1:3]
    shop3 = shopList[3:7]
    shop4 = shopList[7:11]
    context = {'pageTitle': '主页', 'wheelList': wheelList, 'navList': navList, 'mustBuyList': mustBuyList,
               'shop1': shop1, 'shop2': shop2, 'shop3': shop3, 'shop4': shop4, 'mainshowList': mainshowList}
    return render(request, 'App/Home.html', context)


def Market(request):
    # 获取所有类型
    foodtypes = FoodTypes.objects.all()
    # 获取列表商品
    goodsList = Goods.objects.all().filter(categoryid=104749)
    context = {'pageTitle': '闪送超市', 'foodtypes': foodtypes, 'goodsList': goodsList}
    return render(request, 'App/Market.html', context)


def MarketCategory(request, foodtype, childcid, ordering):
    # 获取所有类型
    foodtypes = FoodTypes.objects.all()
    # 获取列表商品
    print('过滤拼接字段:', foodtype)
    if ordering == '0':
        orderRule = 'id'
    elif ordering == '1':
        orderRule = 'price'
    elif ordering == '2':
        orderRule = '-price'
    elif ordering == '3':
        orderRule = 'productnum'
    else:
        orderRule = 'id'

    if childcid == '0':
        goodsList = Goods.objects.all().filter(categoryid=foodtype).order_by(orderRule)
    else:
        goodsList = Goods.objects.all().filter(categoryid=foodtype).filter(childcid=childcid).order_by(orderRule)

    print('查询结果:', len(goodsList))
    childType = FoodTypes.objects.all().filter(typeid=foodtype).first()
    childTypeName = childType.childtypenames
    childTypeAndNames = childTypeName.split('#')
    items = []
    for child in childTypeAndNames:
        children = child.split(':')
        item = {'childName': children[0], 'childType': children[1]}
        items.append(item)

    cartlist = []
    # 判断用户是否登录
    token = request.session.get("token")
    if token:
        user = User.objects.get(userToken=token)
        cartlist = Cart.objects.filter(userAccount=user.userAccount)

    for p in goodsList:
        for c in cartlist:
            if c.productid == p.productid:
                p.num = c.productnum
                continue
    context = {'pageTitle': '闪送超市', 'foodtypes': foodtypes, 'goodsList': goodsList,
               'items': items, 'foodtypeid': foodtype, 'childcid': childcid, 'orderRule': ordering}

    return render(request, 'App/Market.html', context)


def Cart(request):
    context = {'pageTitle': '购物车'}
    return render(request, 'App/Cart.html', context)


def Mine(request):
    user = request.COOKIES.get('users', '点击登录')
    userimg=request.COOKIES.get('')
    context = {'pageTitle': '我的','username': user}
    return render(request, 'App/Mine.html', context)


# 修改购物车
def changecart(request, flag):
    # 判断用户是否登录
    token = request.session.get("token")
    if token == None:
        # 没登录
        return JsonResponse({"data": -1, "status": "error"})

    productid = request.POST.get("productid")
    product = Goods.objects.get(productid=productid)
    user = User.objects.get(userToken=token)

    if flag == '0':
        if product.storenums == 0:
            return JsonResponse({"data": -2, "status": "error"})
        carts = Cart.objects.filter(userAccount=user.userAccount)
        c = None
        if carts.count() == 0:
            # 直接增加一条订单
            c = Cart.createcart(user.userAccount, productid, 1, product.price, True, product.productimg,
                                product.productlongname, False)
            c.save()
            pass
        else:
            try:
                c = carts.get(productid=productid)
                # 修改数量和价格
                c.productnum += 1
                c.productprice = "%.2f" % (float(product.price) * c.productnum)
                c.save()
            except Cart.DoesNotExist as e:
                # 直接增加一条订单
                c = Cart.createcart(user.userAccount, productid, 1, product.price, True, product.productimg,
                                    product.productlongname, False)
                c.save()
        # 库存减一
        product.storenums -= 1
        product.save()
        return JsonResponse({"data": c.productnum, "price": c.productprice, "status": "success"})
    elif flag == '1':
        carts = Cart.objects.filter(userAccount=user.userAccount)
        c = None
        if carts.count() == 0:
            return JsonResponse({"data": -2, "status": "error"})
        else:
            try:
                c = carts.get(productid=productid)
                # 修改数量和价格
                c.productnum -= 1
                c.productprice = "%.2f" % (float(product.price) * c.productnum)
                if c.productnum == 0:
                    c.delete()
                else:
                    c.save()
            except Cart.DoesNotExist as e:
                return JsonResponse({"data": -2, "status": "error"})
        # 库存减一
        product.storenums += 1
        product.save()
        return JsonResponse({"data": c.productnum, "price": c.productprice, "status": "success"})
    elif flag == '2':
        carts = Cart.objects.filter(userAccount=user.userAccount)
        c = carts.get(productid=productid)
        c.isChose = not c.isChose
        c.save()
        str = ""
        if c.isChose:
            str = "√"
        return JsonResponse({"data": str, "status": "success"})


# 注册
def register(request):
    if request.method == "POST":
        userAccount = request.POST.get("userAccount")
        userPasswd = request.POST.get("userPass")
        userName = request.POST.get("userName")
        userPhone = request.POST.get("userPhone")
        userAdderss = request.POST.get("userAdderss")
        # 等级
        userRank = 0
        token = time.time() + random.randrange(1, 100000)
        userToken = str(token)
        f = request.FILES["userImg"]
        fp = os.path.join(settings.MDEIA_ROOT, userAccount + ".png")
        with open(fp, "wb") as userImg:
            for data in f.chunks():
                userImg.write(data)

        user = User.createuser(userAccount, userPasswd, userName, userPhone, userAdderss, userImg, userRank, userToken)
        user.save()

        request.session["username"] = userName
        request.session["token"] = userToken

        return redirect('/mine/')
    else:
        return render(request, 'App/register.html', {"title": "注册"})


# 登录
def Login(request):
    return render(request, 'App/Login.html')

def jumpTwo(request):
    context = {'operate': '登录'}
    return render(request, 'App/jump.html', context)


# 登录检测
def loginCheck(request):
    # 获取用户输入的用户名和密码
    username = request.GET.get('username')
    password = request.GET.get('password')

    users = User.objects.filter(userAccount=username)
    if len(users) == 1:
        if users[0].userPasswd == password:
            userImg=users[0].userImg
            response = HttpResponseRedirect(reverse('axf:mine'))
            response.set_cookie('users', username,userImg, max_age=100000)
            return response
        else:
            context = {'status': 'pwdFalse'}
            # return JsonResponse(context)
    else:
        context = {'status': 'usernameFalse'}
    return JsonResponse(context)

# 退出登陆
from django.contrib.auth import logout


def quit(request):
    response = HttpResponseRedirect(reverse('axf:mine'))
    response.delete_cookie('users')
    return response


# 检测用户名
def checkuserid(request):
    userid = request.POST.get("userid")
    try:
        user = User.objects.get(userAccount=userid)
        return JsonResponse({"data": "改用户已经被注册", "status": "error"})
    except User.DoesNotExist as e:
        return JsonResponse({"data": "可以注册", "status": "success"})
