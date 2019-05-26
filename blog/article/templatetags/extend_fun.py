from django import template
from article.models import Article, Category, Tag, Ads

register = template.Library()


# 自定义的筛选器，把所有的大写字母变成小写
@register.filter(name='mylower')
def mylower(value):
    return value.lower()


# 自定义的筛选器，显示指定长度的内容
@register.filter(name='myslice')
def myslice(value, length):
    result = value[:length]
    return result


# 自定义的模板标签
@register.simple_tag()
def getCategory():
    return Category.objects.all()


# 归档
@register.simple_tag()
def getarchive(num=3):
    result = Article.objects.dates("pub_time", 'month', order='DESC')[:num]
    # print(result)
    return result


# 最新文章
@register.simple_tag()
def get_new_article():
    result = Article.objects.all().order_by("-pub_time")[:3]
    return result


# 标签云
@register.simple_tag()
def get_all_tag():
    result = Tag.objects.all()
    return result

@register.simple_tag()
def get_all_ads():
    result = Ads.objects.all()
    return result