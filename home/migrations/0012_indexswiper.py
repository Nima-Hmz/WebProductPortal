# Generated by Django 4.2 on 2024-10-04 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_delete_services'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndexSwiper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(upload_to='swiper/', verbose_name='تصویر1')),
                ('image2', models.ImageField(upload_to='swiper/', verbose_name='تصویر2')),
                ('image3', models.ImageField(upload_to='swiper/', verbose_name='تصویر3')),
            ],
        ),
    ]
