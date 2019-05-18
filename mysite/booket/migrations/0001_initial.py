# Generated by Django 2.2.1 on 2019-05-18 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='书籍主键')),
                ('book_name', models.CharField(max_length=50, verbose_name='书籍名字')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
            ],
        ),
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='英雄主键')),
                ('hero_name', models.CharField(max_length=50, verbose_name='英雄名字')),
                ('gender', models.CharField(max_length=20, verbose_name='英雄性别')),
                ('skill', models.CharField(max_length=200, verbose_name='英雄技能')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booket.Book', verbose_name='所属书籍')),
            ],
        ),
    ]
