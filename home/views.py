from django.shortcuts import render
from django.views import View
from products.models import Category
from articles.models import Article
from .models import FirstTitle, AboutUs, Services
from .template_manager import language_switcher

# Create your views here.


class IndexView(View):
	def get(self, request):
		lang = request.GET.get('lang', 'fa')
		valid_langs = ['en', 'fa']
		if lang not in valid_langs:
			lang = 'fa'
		first_title = FirstTitle.objects.first()
		aboutus = AboutUs.objects.first()
		services = Services.objects.first()

		context = {

			'index_image1':first_title.image,
			'index_image2':first_title.image2,
			'about_image':aboutus.image,
			'services_title':services.get_title(lang),
			'services_image1':services.image1,
			'services_description1':services.get_description(lang, 1),
			'services_image2':services.image2,
			'services_description2':services.get_description(lang, 2),
			'services_image3':services.image3,
			'services_description3':services.get_description(lang, 3),
			'services_image4':services.image4,
			'services_description4':services.get_description(lang, 4),
			'services_image5':services.image5,
			'services_description5':services.get_description(lang, 5),
			'main_index':True,

		}

		context.update(language_switcher(first_title, lang, "index"))

		for i, obj in enumerate(Category.objects.filter(star=True)[:5], start=1):
			context.update(language_switcher(obj, lang, "category", f"{i}"))
			context.update({f'category_image{i}':obj.image})
			context.update({f'category_slug{i}':obj.slug})

		for i, obj in enumerate(Article.objects.all()[:3], start=1):
			context.update(language_switcher(obj, lang, "article", f"{i}"))
			context.update({f'article_image{i}':obj.thumbnail})
			context.update({f'article_slug{i}':obj.slug})


		return render(request, 'home/index.html', context=context)



class AboutUsView(View):
	def get(self, request):
		lang = request.GET.get('lang', 'fa')
		
		valid_langs = ['en', 'fa']
		if lang not in valid_langs:
			lang = 'fa'

		aboutus = AboutUs.objects.first()
		context = {

			'about_image':aboutus.image,
			'about_temp':True

		}
		context.update(language_switcher(aboutus, lang, "about"))

		return render(request, 'home/aboutus.html', context)
