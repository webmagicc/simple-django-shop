from shop.models import Category, Product
import scrapy
from slugify import slugify
from properties.models import CategoryProperty, ProductProperty
from selenium import webdriver
from django.conf import settings
import uuid
from urllib.request import urlretrieve
import time


class ProductFilterSpider(scrapy.Spider):
    name = "product_filter"