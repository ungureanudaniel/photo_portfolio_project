# Generated by Django 3.1 on 2020-08-14 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo_portfolio_app', '0016_auto_20200814_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='thumbnail',
            field=models.FileField(default='', upload_to='static/photo_portfolio_app/images/'),
        ),
    ]
