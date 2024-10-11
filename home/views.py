from django.shortcuts import render
from django.views import View
from products.models import Category
from articles.models import Article
from .models import FirstTitle, AboutUs, IndexSwiper
from .template_manager import language_switcher

# Create your views here.


class IndexView(View):
	def get(self, request):
		first_title = FirstTitle.objects.first()
		aboutus = AboutUs.objects.first()
		index_swiper = IndexSwiper.objects.first()
		category0 = Category.objects.filter(star=True)[:6]

		context = {

			'index_image1':first_title.image,
			'index_image2':first_title.image2,
			'about_image':aboutus.image,
			'aboutus_title': aboutus.fa_title,
			'about_description':aboutus.fa_description,
			'main_index':True,
			'index_swiper': index_swiper,
			'category0':category0,


		}

		context.update(language_switcher(first_title, "index"))

		for i, obj in enumerate(Category.objects.filter(star=True)[:5], start=1):
			context.update(language_switcher(obj, "category", f"{i}"))
			context.update({f'category_image{i}':obj.image})
			context.update({f'category_slug{i}':obj.slug})

		for i, obj in enumerate(Article.objects.all()[:5], start=1):
			context.update(language_switcher(obj, "article", f"{i}"))
			context.update({f'article_image{i}':obj.thumbnail})
			context.update({f'article_slug{i}':obj.slug})


		return render(request, 'home/index.html', context=context)



class AboutUsView(View):
	def get(self, request):

		aboutus = AboutUs.objects.first()
		context = {

			'about_image':aboutus.image,
			'about_temp':True

		}
		context.update(language_switcher(aboutus, "about"))

		return render(request, 'home/aboutus.html', context)
