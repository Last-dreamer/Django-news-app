# Generated by Django 3.1.5 on 2021-01-30 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_category_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='detail',
        ),
    ]