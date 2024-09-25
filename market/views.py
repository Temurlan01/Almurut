from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.views import View
import datetime
from django.http import Http404
from market.models import Product, ProductRating, ProductGallery


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = {
            'Product': Product.objects.all(),
        }
        return context


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

    def get_context_data(self, **kwargs):
        try:
            product = Product.objects.get(id=kwargs['pk'])
        except Product.DoesNotExist:
            raise Http404
        product_category = product.category
        category_other_product_list = (
            Product.objects
            .filter(category=product_category)
            .exclude(id=product.id)
        )
        context = {
            'product': product,
            'other_products': category_other_product_list,
            'other_products_len': len(category_other_product_list)



        }
        return context


class ProductListView(TemplateView):
    template_name = 'product-list.html'

    def get_context_data(self, **kwargs):

        context = {
            'Product_list': Product.objects.all(),
            'now': datetime.datetime.now().date()
        }
        return context


class ShoppingCartView(TemplateView):
    template_name = 'shopping-cart.html'


class SendProductFeedbackView(View):

    def post(self, request, *args, **kwargs):
        data = request.POST
        rating_value = data['rating_value']
        comment = data['comment']
        name = data['name']
        email = data['email']

        product = Product.objects.get(id=kwargs['pk'])
        user = request.user
        if user.is_authenticated:

            ProductRating.objects.create(
                stars=rating_value,
                your_review=comment,
                name=name,
                Email=email,
                product=product,
                user=user,
            )
            return redirect('product-detail-url', pk=product.id )
        else:
            return redirect('/login/')