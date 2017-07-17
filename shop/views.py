from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Product, Category

class HomeView(ListView):
	model = Product
	queryset = Product.objects.filter(promo=1)
	template_name = 'shop/home.html'


class CategoryView(DetailView):
	model = Category
	queryset = Category.objects.all()
	template_name = 'shop/category.html'
	
