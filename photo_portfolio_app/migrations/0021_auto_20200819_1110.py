# Generated by Django 3.1 on 2020-08-19 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo_portfolio_app', '0020_auto_20200819_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='category',
            field=models.CharField(default='', max_length=200),
        ),
    ]
