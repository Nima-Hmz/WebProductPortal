from django.db import models
from tinymce.models import HTMLField

# Create your models here.


class FirstTitle(models.Model):
	fa_title = models.CharField(verbose_name='عنوان', max_length=200)
	fa_description = HTMLField(verbose_name='توضیحات')
	image = models.ImageField(upload_to='first_title/', verbose_name=("تصویر 1"))
	image2 = models.ImageField(upload_to='first_title/', verbose_name=("تصویر 2 آپشنال"), null=True, blank=True)


	def __str__(self):
		return self.fa_title

	class Meta:
		verbose_name = ("صفحه اصلی")
		verbose_name_plural = ("صفحه اصلی")


class AboutUs(models.Model):
	fa_title = models.CharField(verbose_name='عنوان', max_length=200)
	fa_description = HTMLField(verbose_name='توضیحات')
	image = models.ImageField(upload_to='about_us/', verbose_name=("تصویر"))

	def __str__(self):
		return self.fa_title

	class Meta:
		verbose_name = ("درباره ما")
		verbose_name_plural = ('درباره ما')


class ContactUs(models.Model):
	fa_title = models.CharField(verbose_name='عنوان', max_length=200)
	phone_number = models.CharField(max_length=200, verbose_name='شماره تماس')
	email = models.EmailField(verbose_name='ایمیل')
	fa_description = models.TextField(verbose_name='آدرس')
	location = models.TextField(verbose_name='موقعیت مکانی')


	def __str__(self):
		return self.fa_title

	class Meta:
		verbose_name = ("تماس با ما")
		verbose_name_plural = ('تماس با ما')

class IndexSwiper(models.Model):
	image1 = models.ImageField(upload_to='swiper/', verbose_name=("تصویر1"))
	image2 = models.ImageField(upload_to='swiper/', verbose_name=("تصویر2"))
	image3 = models.ImageField(upload_to='swiper/', verbose_name=("تصویر3"))

	def __str__(self):
		return "تصویر اسلایدر"

	class Meta:
		verbose_name = ("اسلاید صفحه اول")
		verbose_name_plural = ('اسلاید صفحه اول')



class Updating(models.Model):
	status = models.BooleanField(default=False, verbose_name='فعال کردن وضعیت توسعه')
	title = models.CharField(max_length=200, verbose_name='عنوان')
	description = HTMLField(verbose_name='توضیحات')

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = ("وضعیت توسعه")
		verbose_name_plural = ('وضعیت توسعه')

