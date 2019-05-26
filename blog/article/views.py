from django.shortcuts import render,redirect,reverse
from django.core.paginator import Paginator
from django.core.mail import send_mail, EmailMultiAlternatives
from .models import Article, MessageInfo, Ads
import markdown
from comments.forms import CommentForm
from django.conf import settings
from django.views.generic import View


# Create your views here.
def my_page(article, pagenum):
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

    page = my_page(article, pagenum)
    return render(request, 'index.html', {'page': page})


def category(request, id):
    # 获取当前页数
    pagenum = request.GET.get('page')
    # 如果当前页数为None 则pagenum的值为1
    pagenum = 1 if pagenum == None else pagenum
    article = Article.objects.filter(category__id=id).order_by('-look_num')
    page = my_page(article, pagenum)
    page.parms = "/category/%s/" % (id,)
    return render(request, 'index.html', {"page": page})


def archive(request, year, month):
    # 获取当前页数
    pagenum = request.GET.get('page')
    # 如果当前页数为None 则pagenum的值为1
    pagenum = 1 if pagenum == None else pagenum
    article = Article.objects.filter(pub_time__year=year, pub_time__month=month).order_by('-look_num')
    page = my_page(article, pagenum)
    page.parms = "/archive/%s/%s/" % (year, month,)
    return render(request, 'index.html', {'page': page})


def tag(request, id):
    # 获取当前页数
    pagenum = request.GET.get('page')

    # 如果当前页数为None 则pagenum的值为1
    pagenum = 1 if pagenum == None else pagenum
    article = Article.objects.filter(tag__id=id).order_by("-look_num")
    page = my_page(article, pagenum)
    page.parms = "/tag/%s/" % (id,)
    return render(request, 'index.html', {'page': page})


def detail(request, id):
    article = Article.objects.filter(pk=id).first()
    article.look_num += 1
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
    if request.method == 'GET':
        return render(request, 'contact.html', {'msg': '输入信息'})
    else:
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        info = request.POST.get('info')
        url = "<a href='http://www.baidu.com'>百度一下你就知道</a>"

        try:
            msg = EmailMultiAlternatives('测试邮件', url, settings.DEFAULT_FROM_EMAIL, ['18438622728@163.com'])
            msg.content_subtype = 'html'
            msg.send()
        except Exception as e:
            print(e)

        msge = MessageInfo(username=name, email=email, subject=subject, info=info)
        msge.save()

        return render(request, 'contact.html', {'msg': '发送成功！'})


class Add(View):
    def get(self, request):
        return render(request, 'img.html')

    def post(self, request):
        img = request.FILES['img']
        desc = request.POST.get('desc')
        ads = Ads(img=img, desc=desc)
        ads.save()
        return redirect(reverse('article:index'))
