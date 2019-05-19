from django.db import models

# Create your models here.

class Book(models.Model):
    id=models.AutoField(primary_key=True,verbose_name='书籍主键')
    book_name=models.CharField(max_length=50,verbose_name='书籍名字')
    author=models.CharField(max_length=50,default='1',verbose_name='书籍作者')
    type=models.CharField(max_length=50,default='1',verbose_name='类型')
    time=models.DateTimeField(auto_now_add=True,verbose_name='添加时间')

    def __str__(self):
        return self.book_name

class Hero(models.Model):
    id=models.AutoField(primary_key=True,verbose_name='英雄主键')
    hero_name=models.CharField(max_length=50,verbose_name='英雄名字')
    gender=models.CharField(max_length=20,verbose_name='英雄性别')
    skill=models.CharField(max_length=200,verbose_name='英雄技能')
    book=models.ForeignKey(Book,models.CASCADE,verbose_name='所属书籍')

    def __str__(self):
        return self.hero_name