# Generated by Django 2.2.1 on 2019-05-26 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_messageinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ads',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='图片主键')),
                ('img', models.ImageField(upload_to='ads', verbose_name='图片')),
                ('desc', models.CharField(max_length=30, verbose_name='图片描述')),
            ],
            options={
                'verbose_name': '轮播图',
                'verbose_name_plural': '轮播图',
            },
        ),
    ]