# Generated by Django 3.1.2 on 2020-11-19 10:36

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_site', '0010_auto_20201119_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]