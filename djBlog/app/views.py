from django.shortcuts import render
import time
# Create your views here.
from app import models
from app.models import Article


def base(request):
    return render(request,'pubarticle.html')
def success(request):
    aname = request.POST.get('aname')
    acontent = request.POST.get('acontent')
    author = request.POST.get('author')
    shijian = time.strftime('%Y-%m-%d', time.localtime())
    article = Article(aname=aname, acontent=acontent, aauthor=author, atime=shijian)
    article.save()
    return render(request,'success.html')
def showarticle(request):
    articles=Article.objects.all()
    # for article in articles:
    art={'articles':articles}
    return render(request,'show.html',art)