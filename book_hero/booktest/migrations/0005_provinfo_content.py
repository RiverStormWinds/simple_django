# Generated by Django 2.0.6 on 2018-07-02 04:00

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0004_auto_20180627_1917'),
    ]

    operations = [
        migrations.AddField(
            model_name='provinfo',
            name='content',
            field=tinymce.models.HTMLField(default='test', verbose_name='文章详情'),
        ),
    ]
