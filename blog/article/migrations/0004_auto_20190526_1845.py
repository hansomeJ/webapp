# Generated by Django 2.2.1 on 2019-05-26 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_ads'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='img',
            field=models.ImageField(upload_to='img', verbose_name='图片'),
        ),
    ]
