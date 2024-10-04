from django.contrib import admin

# Register your models here.

from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('fa_title', 'slug', 'star')
    search_fields = ("fa_title", "slug")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('fa_title', 'slug',  'available', 'position', 'pub_date')
    search_fields = ("fa_title", "slug")
    list_filter = ("available",)