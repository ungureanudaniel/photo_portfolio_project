# Generated by Django 3.1 on 2020-08-13 21:58

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('photo_portfolio_app', '0006_remove_photo_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
