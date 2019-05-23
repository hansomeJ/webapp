from django import template
from article.models import Article, Category, Tag

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