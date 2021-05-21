# Generated by Django 3.1 on 2021-05-21 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo_portfolio_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(default='', max_length=200, unique=True)),
                ('text', models.TextField()),
                ('thumbnail', models.ImageField(default='', upload_to='static/photo_portfolio_app/categ_images/')),
                ('specialties', models.BooleanField(blank=True, default=False)),
            ],
        ),
    ]
