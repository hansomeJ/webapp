from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Article
import markdown

# Create your views here.


def index(request):
    # 获取当前页数
    pagenum=request.GET.get('page')
    num=request.GET.get('num')
    # 如果当前页数为None 则pagenum的值为1
    pagenum=1 if pagenum==None else pagenum
    num=1 if num==None else num
    print(pagenum,num)

    article=Article.objects.all().order_by("-look_num")

    mk = markdown.Markdown(extensions=[
        "markdown.extensions.extra",
        "markdown.extensions.codehilite",
        "markdown.extensions.toc"
    ])
    for a in article:
        a.content = mk.convert(a.content)
    # 实例化一个pageinator对象
    paginator=Paginator(article,num)
    #生成一个page对象
    page=paginator.get_page(pagenum)

    return render(request,'index.html',{'page':page})
def detail(request,id):
    article=Article.objects.filter(pk=id).first()

    mk = markdown.Markdown(extensions=[
        "markdown.extensions.extra",
        "markdown.extensions.codehilite",
        "markdown.extensions.toc"
    ])
    article.content=mk.convert(article.content)
    article.toc=mk.toc
    return render(request,'single.html',locals())

