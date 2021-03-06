# Generated by Django 2.2.1 on 2019-05-22 03:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='评论主键')),
                ('username', models.CharField(max_length=30, verbose_name='评论人名字')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='评论人邮箱')),
                ('url', models.URLField(blank=True, null=True, verbose_name='评论人主页')),
                ('content', models.CharField(max_length=500, verbose_name='评论内容')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.Article', verbose_name='评论的文章')),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
            },
        ),
    ]
