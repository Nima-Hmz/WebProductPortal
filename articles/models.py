from django.db import models
from tinymce.models import HTMLField
from django.utils import timezone
from extensions.utils import jalali_converter

# Create your models here.


class Category(models.Model):
    """
    Category model that holds some sorts of categories that used in the blog
    """

    fa_title = models.CharField(max_length=200, verbose_name=("عنوان دسته‌بندی"))
    en_title = models.CharField(max_length=200, verbose_name=("عنوان دسته‌بندی انگلیسی"))
    slug = models.SlugField(max_length=100, unique=True, verbose_name=("آدرس دسته‌بندی"))


    def __str__(self):
        return self.fa_title

    def get_title(self, lang='fa'):
        return getattr(self, f'{lang}_title', self.fa_title)

    class Meta:
        verbose_name = ("دسته‌بندی")
        verbose_name_plural = ("دسته‌بندی ها")
        ordering = ['id']


class Article(models.Model):
    """
    Article model that holds information about articles published on the blog.
    """
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=("دسته بندی"), help_text=("دسته بندی پست خود را وارد کنید"), related_name="blog")
    fa_title = models.CharField(max_length=200, verbose_name=("عنوان مقاله"), help_text=("عنوان مقاله را وارد کنید"))
    en_title = models.CharField(max_length=200, verbose_name=("عنوان مقاله انگلیسی"), help_text=("عنوان مقاله را وارد کنید انگلیسی"))
    slug = models.SlugField(max_length=100, verbose_name=("آدرس مقاله"),unique=True, help_text=("آدرس مقاله را میتوانید از اینجا عوض کنید،(نکته: فقط در زمان ویرایش مقاله امکان تغییر آدرس وجود دارد) اما با عوض کردن آن آدرس قبلی در دسترس نخواهد بود"))
    fa_description = HTMLField(verbose_name=("مقاله"), help_text=("محتوای مقاله را وارد کنید"))
    en_description = HTMLField(verbose_name=("مقاله انگلیسی"), help_text=("محتوای مقاله را وارد کنید انگلیسی"))
    thumbnail = models.ImageField(upload_to='articles/', verbose_name=("تصویر مقاله"), help_text=("تصویری که میخواهید به عنوان کاور مقاله قرار بگیرد را وارد کنید"))
    pub_date = models.DateTimeField(default=timezone.now, verbose_name=("زمان انتشار"))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True, verbose_name=("وضعیت انتشار"))

    def __str__(self):
        return self.fa_title

    def get_title(self, lang='fa'):
        return getattr(self, f'{lang}_title', self.fa_title)

    def get_description(self, lang=''):
        return getattr(self, f'{lang}_description', self.fa_description)

    class Meta:
        verbose_name = ("مقاله")
        verbose_name_plural = ("مقالات")
        ordering = ['-pub_date']

    def jpub_date(self):
        return jalali_converter(self.pub_date)
        
    





