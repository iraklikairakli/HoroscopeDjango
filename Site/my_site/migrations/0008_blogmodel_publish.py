# Generated by Django 3.1.2 on 2020-11-11 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_site', '0007_auto_20201109_1841'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmodel',
            name='publish',
            field=models.DateField(null=True),
        ),
    ]