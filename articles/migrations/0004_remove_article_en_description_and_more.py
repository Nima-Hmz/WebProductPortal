# Generated by Django 4.2 on 2024-10-04 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_alter_category_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='en_description',
        ),
        migrations.RemoveField(
            model_name='article',
            name='en_title',
        ),
        migrations.RemoveField(
            model_name='category',
            name='en_title',
        ),
    ]
