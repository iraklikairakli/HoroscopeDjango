# Generated by Django 3.1.2 on 2020-11-19 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_site', '0013_blogmodel_blog_views'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogmodel',
            name='blog_views',
        ),
    ]
