from django.shortcuts import render
from django.views import View
from django.shortcuts import get_object_or_404
from .models import Product, Category

# Create your views here.



class ProductsView(View):
	def get(self, request):

		root_categories = Category.objects.filter(parent__isnull=True)
		context = {

			'root_categories':root_categories,

		}
			
		return render(request, 'products/products.html', context)


class ProductListView(View):
	def get(self, request, slug):

		category = get_object_or_404(Category, slug=slug)
		products = category.products.all()
		context = {

			'products':products,
			'cat_title':category.fa_title,

		}
		return render(request, 'products/product_list.html', context)


class ProductDetailView(View):
	def get(self, request, slug):

		product = get_object_or_404(Product, slug=slug)
		context = {
		
			'product':product

		}
		return render(request, 'products/product_detail.html', context)
