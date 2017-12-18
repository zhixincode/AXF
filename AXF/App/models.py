from django.db import models

# Create your models here.
class Register(models.Model):
    username=models.CharField(max_length=15)
    password=models.CharField(max_length=10)
class Wheel(models.Model):
    img=models.CharField(max_length=200)
    name=models.CharField(max_length=20)
    trackid=models.CharField(max_length=20)
    class Meta:
        db_table='axf_wheel'
class Nav(models.Model):
    img=models.CharField(max_length=200)
    name=models.CharField(max_length=20)
    trackid=models.CharField(max_length=20)
    class Meta:
        db_table='axf_nav'
class MustBuy(models.Model):
    img=models.CharField(max_length=200)
    name=models.CharField(max_length=20)
    trackid=models.CharField(max_length=20)
    class Meta:
        db_table='axf_mustbuy'
class Shop(models.Model):
    img=models.CharField(max_length=200)
    name=models.CharField(max_length=20)
    trackid=models.CharField(max_length=20)
    class Meta:
        db_table='axf_shop'
"""
trackid,name,img,categoryid,brandname,img1,childcid1,productid1,longname1,
price1,marketprice1,img2,childcid2,productid2,longname2,price2,marketprice2,
img3,childcid3,productid3,longname3,price3,marketprice3
"""
class MainShow(models.Model):
    trackid = models.CharField(max_length=20)
    name=models.CharField(max_length=20)
    img = models.CharField(max_length=200)
    categoryid=models.CharField(max_length=20)
    brandname = models.CharField(max_length=20)
    img1=models.CharField(max_length=200)
    childcid1 = models.CharField(max_length=20)
    productid1=models.CharField(max_length=20)
    longname1 = models.CharField(max_length=50)
    price1 = models.CharField(max_length=20)
    marketprice1 = models.CharField(max_length=20)
    img2 = models.CharField(max_length=200)
    childcid2 = models.CharField(max_length=20)
    productid2 = models.CharField(max_length=20)
    longname2 = models.CharField(max_length=50)
    price2 = models.CharField(max_length=20)
    marketprice2 = models.CharField(max_length=20)
    img3 = models.CharField(max_length=200)
    childcid3 = models.CharField(max_length=20)
    productid3 = models.CharField(max_length=20)
    longname3 = models.CharField(max_length=50)
    price3 = models.CharField(max_length=20)
    marketprice3 = models.CharField(max_length=20)


    class Meta:
        db_table='axf_mainshow'
# typeid,typename,childtypenames,typesort
class FoodTypes(models.Model):
    typeid=models.CharField(max_length=20)
    typename=models.CharField(max_length=100)
    childtypenames=models.CharField(max_length=200)
    typesort=models.CharField(max_length=200)
    class Meta:
        db_table='axf_foodtypes'
"""
productid,productimg,productname,productlongname,isxf,pmdesc,
specifics,price,marketprice,categoryid,childcid,childcidname,
dealerid,storenums,productnum
"""
class Goods(models.Model):
    productid=models.CharField(max_length=30)
    productimg = models.CharField(max_length=200)
    productname = models.CharField(max_length=200)
    productlongname = models.CharField(max_length=200)
    isxf = models.BooleanField(default=False)
    pmdesc = models.CharField(max_length=30)
    specifics = models.CharField(max_length=100)
    price = models.FloatField()
    marketprice = models.FloatField()
    categoryid = models.CharField(max_length=20)
    childcid = models.CharField(max_length=200)
    childcidname = models.CharField(max_length=20)
    dealerid = models.CharField(max_length=200)
    storenums = models.IntegerField()
    productnum = models.CharField(max_length=200)
    class Meta:
        db_table='axf_goods'
#用户模型
class User(models.Model):
    # 用户账号，要唯一
    userAccount = models.CharField(max_length=20,unique=True)
    # 密码
    userPasswd  = models.CharField(max_length=20)
    # 昵称
    userName    =  models.CharField(max_length=20)
    # 手机号
    userPhone   = models.CharField(max_length=20)
    # 地址
    userAdderss = models.CharField(max_length=100)
    # 头像路径
    userImg     = models.CharField(max_length=150)
    # 等级
    userRank    = models.IntegerField()
    # touken验证值，每次登陆之后都会更新
    userToken   = models.CharField(max_length=50)
    @classmethod
    def createuser(cls,account,passwd,name,phone,address,img,rank,token):
        u = cls(userAccount = account,userPasswd = passwd,userName=name,userPhone=phone,userAdderss=address,userImg=img,userRank=rank,userToken=token)
        return u
class CartManager1(models.Manager):
    def get_queryset(self):
        return super(CartManager1, self).get_queryset().filter(isDelete=False)
class CartManager2(models.Manager):
    def get_queryset(self):
        return super(CartManager2, self).get_queryset().filter(isDelete=True)
class Cart(models.Model):
    userAccount = models.CharField(max_length=20)
    productid = models.CharField(max_length=10)
    productnum = models.IntegerField()
    productprice = models.CharField(max_length=10)
    isChose = models.BooleanField(default=True)
    productimg = models.CharField(max_length=150)
    productname = models.CharField(max_length=100)
    orderid = models.CharField(max_length=20,default="0")
    isDelete = models.BooleanField(default=False)
    objects = CartManager1()
    obj2 = CartManager2()
    @classmethod
    def createcart(cls,userAccount,productid,productnum,productprice,isChose,productimg,productname,isDelete):
        c = cls(userAccount = userAccount,productid = productid,productnum=productnum,productprice=productprice,isChose=isChose,productimg=productimg,productname=productname,isDelete=isDelete)
        return c
class Order(models.Model):
    orderid = models.CharField(max_length=20)
    userid  = models.CharField(max_length=20)
    progress = models.IntegerField()

    @classmethod
    def createorder(cls, orderid, userid, progress):
        o = cls(orderid=orderid, userid=userid, progress=progress)
        return o