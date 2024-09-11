from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'index.html'


class FaqView(TemplateView):
    template_name = 'faq.html'


class ErrorView(TemplateView):
    template_name = '404.html'


class FavoritesView(TemplateView):
    template_name = 'favorites.html'


class LoginView(TemplateView):
    template_name = 'login.html'


class ProductDetailView(TemplateView):
    template_name = 'product-detail.html'


class ProductListView(TemplateView):
    template_name = 'product-list.html'


class ShoppingCartView(TemplateView):
    template_name = 'shopping-cart.html'
