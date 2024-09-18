# Generated by Django 5.0 on 2024-09-05 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_rename_en_description_article_endescription_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['id'], 'verbose_name': 'دسته\u200cبندی', 'verbose_name_plural': 'دسته\u200cبندی ها'},
        ),
        migrations.RenameField(
            model_name='article',
            old_name='endescription',
            new_name='en_description',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='entitle',
            new_name='en_title',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='description',
            new_name='fa_description',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='title',
            new_name='fa_title',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='entitle',
            new_name='en_title',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='title',
            new_name='fa_title',
        ),
    ]
