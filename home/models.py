from django.db import models
from tinymce.models import HTMLField

# Create your models here.


class FirstTitle(models.Model):
	fa_title = models.CharField(verbose_name='عنوان', max_length=200)
	en_title = models.CharField(verbose_name='عنوان انگلیسی', max_length=200)
	fa_description = HTMLField(verbose_name='توضیحات')
	en_description = HTMLField(verbose_name='توضیحات انگلیسی')
	image = models.ImageField(upload_to='first_title/', verbose_name=("تصویر 1"))
	image2 = models.ImageField(upload_to='first_title/', verbose_name=("تصویر 2 آپشنال"), null=True, blank=True)


	def __str__(self):
		return self.fa_title

	def get_title(self, lang='fa'):
		return getattr(self, f'{lang}_title', self.fa_title)

	def get_description(self, lang='fa'):
		return getattr(self, f'{lang}_description', self.fa_description)

	class Meta:
		verbose_name = ("صفحه اصلی")
		verbose_name_plural = ("صفحه اصلی")


class AboutUs(models.Model):
	fa_title = models.CharField(verbose_name='عنوان', max_length=200)
	en_title = models.CharField(verbose_name='عنوان انگلیسی', max_length=200)
	fa_description = HTMLField(verbose_name='توضیحات')
	en_description = HTMLField(verbose_name='توضیحات انگلیسی')
	image = models.ImageField(upload_to='about_us/', verbose_name=("تصویر"))

	def __str__(self):
		return self.fa_title

	def get_title(self, lang='fa'):
		return getattr(self, f'{lang}_title', self.fa_title)

	def get_description(self, lang='fa'):
		return getattr(self, f'{lang}_description', self.fa_description)

	class Meta:
		verbose_name = ("درباره ما")
		verbose_name_plural = ('درباره ما')


class ContactUs(models.Model):
	fa_title = models.CharField(verbose_name='عنوان', max_length=200)
	en_title = models.CharField(verbose_name='عنوان انگلیسی', max_length=200)
	phone_number = models.CharField(max_length=200, verbose_name='شماره تماس')
	email = models.EmailField(verbose_name='ایمیل')
	fa_description = models.TextField(verbose_name='آدرس')
	en_description = models.TextField(verbose_name='آدرس انگلایسی')
	location = models.TextField(verbose_name='موقعیت مکانی')


	def __str__(self):
		return self.fa_title

	def get_title(self, lang='fa'):
		return getattr(self, f'{lang}_title', self.fa_title)

	def get_description(self, lang='fa'):
		return getattr(self, f'{lang}_description', self.fa_description)

	class Meta:
		verbose_name = ("تماس با ما")
		verbose_name_plural = ('تماس با ما')



class Services(models.Model):
	fa_title = models.CharField(verbose_name='عنوان', max_length=200)
	en_title = models.CharField(verbose_name='عنوان انگلیسی', max_length=200)

	image1 = models.TextField(verbose_name=("تصویر1 از سمت چپ"))
	fa_description1 = models.CharField(verbose_name='توضیحات عکس ۱', max_length=200)
	en_description1 = models.CharField(verbose_name='توضیحات عکس ۱ انگلیسی', max_length=200)

	image2 = models.TextField(verbose_name=("تصویر2 از سمت چپ"))
	fa_description2 = models.CharField(verbose_name='توضیحات عکس 2', max_length=200)
	en_description2 = models.CharField(verbose_name='توضیحات عکس 2 انگلیسی', max_length=200)

	image3 = models.TextField(verbose_name=("تصویر3 از سمت چپ"))
	fa_description3 = models.CharField(verbose_name='توضیحات عکس 3', max_length=200)
	en_description3 = models.CharField(verbose_name='توضیحات عکس 3 انگلیسی', max_length=200)

	image4 = models.TextField(verbose_name=("تصویر4 از سمت چپ"))
	fa_description4 = models.CharField(verbose_name='توضیحات عکس 4', max_length=200)
	en_description4 = models.CharField(verbose_name='توضیحات عکس 4 انگلیسی', max_length=200)

	image5 = models.TextField(verbose_name=("تصویر5 از سمت چپ"))
	fa_description5 = models.CharField(verbose_name='توضیحات عکس 5', max_length=200)
	en_description5 = models.CharField(verbose_name='توضیحات عکس 5 انگلیسی', max_length=200)


	def __str__(self):
		return self.fa_title

	def get_title(self, lang='fa'):
		return getattr(self, f'{lang}_title', self.fa_title)

	def get_description(self, lang='fa', number=1):
		return getattr(self, f'{lang}_description{number}', self.fa_description1)

	class Meta:
		verbose_name = ("خدمات")
		verbose_name_plural = ('خدمات')


class Updating(models.Model):
	status = models.BooleanField(default=False, verbose_name='فعال کردن وضعیت توسعه')
	title = models.CharField(max_length=200, verbose_name='عنوان')
	description = HTMLField(verbose_name='توضیحات')

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = ("وضعیت توسعه")
		verbose_name_plural = ('وضعیت توسعه')