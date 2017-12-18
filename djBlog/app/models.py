from django.db import models

# Create your models here.
class Article(models.Model):
    #文章编号
    aid=models.BigAutoField(primary_key=True)
    #文章标题
    aname=models.CharField(max_length=50)
    #文章内容
    acontent=models.TextField()
    #文章作者
    aauthor=models.CharField(max_length=50)
    #发表时间
    atime=models.DateField()
class Review(models.Model):
    #评论id
    reid=models.IntegerField(primary_key=True)
    #评论内容
    recontent=models.TextField()
    #评论的文章
    rearticle=models.ForeignKey(Article)