# Generated by Django 3.1 on 2021-05-24 13:54

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('photo_portfolio_app', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='', upload_to='images/')),
                ('image_title', models.CharField(max_length=200, verbose_name='A short title, max two words')),
                ('description', models.TextField(default='', max_length=500, verbose_name='A short description...')),
                ('date_taken', models.DateField(auto_now_add=True)),
                ('slug', models.SlugField(default='', max_length=100, unique=True)),
                ('featured', models.BooleanField(default=False, verbose_name='Check this if you want picture to be shown as featured on the home page')),
                ('category', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='photo', to='photo_portfolio_app.category')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'ordering': ['-date_taken'],
            },
        ),
    ]
