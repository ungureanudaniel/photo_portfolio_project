# Generated by Django 3.1 on 2020-08-14 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo_portfolio_app', '0011_delete_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
