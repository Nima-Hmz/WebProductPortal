from django.shortcuts import render
from django.views import View
from products.models import Category
from articles.models import Article
from .models import FirstTitle, AboutUs, IndexSwiper

# Create your views here.


class IndexView(View):
	def get(self, request):
		first_title = FirstTitle.objects.first()
		aboutus = AboutUs.objects.first()
		index_swiper = IndexSwiper.objects.first()
		category0 = Category.objects.filter(star=True)[:6]
		article0 = Article.objects.all()[:4]

		context = {

			'index_image1':first_title.image,
			'index_image2':first_title.image2,
			'about_image':aboutus.image,
			'aboutus_title': aboutus.fa_title,
			'about_description':aboutus.fa_description,
			'main_index':True,
			'index_swiper': index_swiper,
			'category0':category0,
			'article0':article0,
			'index_title':first_title.fa_title,
			'index_description':first_title.fa_description


		}


		return render(request, 'home/index.html', context=context)



class AboutUsView(View):
	def get(self, request):

		aboutus = AboutUs.objects.first()
		context = {

			'about':aboutus,
			'about_temp':True

		}

		return render(request, 'home/aboutus.html', context)
