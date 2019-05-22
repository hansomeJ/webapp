from django.db import models
from article.models import Article


# Create your models here.
class Comment(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='评论主键')
    username = models.CharField(max_length=30, verbose_name='评论人名字')
    email = models.EmailField(blank=True, null=True, verbose_name='评论人邮箱')
    url = models.URLField(blank=True, null=True, verbose_name='评论人主页')
    content = models.CharField(max_length=500, verbose_name='评论内容')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='评论的文章')

    class Meta():
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.article
