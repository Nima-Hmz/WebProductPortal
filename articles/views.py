from django.shortcuts import render
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.views import View
from .models import Article

# Create your views here.


class ArticleListView(View):
	def get(self, request):
		articles = Article.objects.filter(status=True)
		paginator = Paginator(articles, 6)
		page = request.GET.get('page')
		article_list1 = paginator.get_page(page)
		context = {

			'article_temp':True,
			'article_list1':article_list1,


		}
		return render(request, 'articles/article_list.html', context)


class ArticleDetailView(View):
	def get(self, request, slug):

		article = get_object_or_404(Article, slug=slug)
		context = {

			'title':article.fa_title,
			'description':article.fa_description,
			'image':article.thumbnail,
			'pub_date':article.pub_date,
			'category':article.category,
			'article_temp':True,


		}
		return render(request, 'articles/article_detail.html', context)