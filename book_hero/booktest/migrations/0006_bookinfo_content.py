# Generated by Django 2.0.6 on 2018-07-02 06:06

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0005_provinfo_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinfo',
            name='content',
            field=tinymce.models.HTMLField(default='test', verbose_name='文章详情'),
        ),
    ]
