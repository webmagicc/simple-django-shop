from django.shortcuts import render
from django.views.generic import ListView
from .models import Product

class HomeView(ListView):
	model = Product
	queryset = Product.objects.filter(promo=1)
	template_name = 'shop/home.html'


class CategoryView(ListView):
	model = Product
	queryset = Product.objects.all()
	template_name = 'shop/category.html'
