# Generated by Django 2.2.7 on 2020-08-15 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.CharField(blank=True, max_length=10000),
        ),
    ]