from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Article
import markdown
from comments.forms import CommentForm


# Create your views here.
def my_page(article,pagenum):
    mk = markdown.Markdown(extensions=[
        "markdown.extensions.extra",
        "markdown.extensions.codehilite",
        "markdown.extensions.toc"
    ])
    for a in article:
        a.content = mk.convert(a.content)
    # 实例化一个pageinator对象
    paginator = Paginator(article, 2)
    # 生成一个page对象
    page = paginator.get_page(pagenum)
    return page

def index(request):
    # 获取当前页数
    pagenum = request.GET.get('page')


    # 如果当前页数为None 则pagenum的值为1
    pagenum = 1 if pagenum == None else pagenum

    # 如果年份和月份都不为空的话就按照获取的年份与月份来查询文章
    article = Article.objects.all().order_by("-look_num")

    page=my_page(article,pagenum)
    return render(request, 'index.html', {'page': page})

def category(request,id):
    # 获取当前页数
    pagenum = request.GET.get('page')
    # 如果当前页数为None 则pagenum的值为1
    pagenum = 1 if pagenum == None else pagenum
    article = Article.objects.filter(category__id=id).order_by('-look_num')
    page =my_page(article,pagenum)
    page.parms = "/category/%s/" % (id,)
    return render(request,'index.html',{"page":page})
def archive(request,year,month):
    # 获取当前页数
    pagenum = request.GET.get('page')
    # 如果当前页数为None 则pagenum的值为1
    pagenum = 1 if pagenum == None else pagenum
    article=Article.objects.filter(pub_time__year=year,pub_time__month=month).order_by('-look_num')
    page=my_page(article,pagenum)
    page.parms = "/archive/%s/%s/" % (year,month,)
    return render(request,'index.html',{'page':page})
def tag(request,id):
    # 获取当前页数
    pagenum = request.GET.get('page')

    # 如果当前页数为None 则pagenum的值为1
    pagenum = 1 if pagenum == None else pagenum
    article = Article.objects.filter(tag__id=id).order_by("-look_num")
    page = my_page(article,pagenum)
    page.parms = "/tag/%s/" % (id,)
    return render(request, 'index.html', {'page': page})
def detail(request, id):
    article = Article.objects.filter(pk=id).first()
    article.look_num+=1
    article.save()
    mk = markdown.Markdown(extensions=[
        "markdown.extensions.extra",
        "markdown.extensions.codehilite",
        "markdown.extensions.toc"
    ])
    article.content = mk.convert(article.content)
    article.toc = mk.toc
    cf = CommentForm()
    return render(request, 'single.html', locals())

def contact(request):
    return render(request,'contact.html')