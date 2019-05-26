from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField


# Create your models here.
# 标签表
class Tag(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='标签主键')
    title = models.CharField(max_length=30, verbose_name='文章标签')

    class Meta():
        verbose_name = '文章标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


# 分类表
class Category(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='分类主键')
    title = models.CharField(max_length=50, verbose_name='文章分类')

    class Meta():
        verbose_name = '文章分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


# 文章表
class Article(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='文章主键')
    tag = models.ManyToManyField(Tag, verbose_name='文章标签')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='文章分类')
    title = models.CharField(max_length=50, verbose_name='文章标题')
    content = models.TextField(verbose_name='文章内容')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='文章作者')
    pub_time = models.DateTimeField(auto_now_add=True, verbose_name='发表时间')
    upd_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    look_num = models.PositiveIntegerField(verbose_name='访问量')

    class Meta():
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class MessageInfo(models.Model):
    username = models.CharField(max_length=30, verbose_name='用户名')
    email = models.EmailField(blank=True, null=True, verbose_name='邮箱')
    subject = models.CharField(max_length=50, verbose_name='主题')
    info = HTMLField(verbose_name='信息')

    class Meta():
        verbose_name = '信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.subject
