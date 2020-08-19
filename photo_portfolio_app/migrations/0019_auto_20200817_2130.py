# Generated by Django 3.1 on 2020-08-17 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo_portfolio_app', '0018_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='description',
            field=models.TextField(default='', max_length=500, verbose_name='A short description...'),
        ),
        migrations.AlterField(
            model_name='category',
            name='specialties',
            field=models.BooleanField(default=False, verbose_name='Check here if you want this photos category to be included in your "specialties", on the home page and services page, otherwise if unchecked it will appear in "Other services"'),
        ),
    ]
