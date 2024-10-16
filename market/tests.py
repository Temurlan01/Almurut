from datetime import datetime
from django.test import TestCase
from market.models import Product, ProductCategory

class ProductListTestCase(TestCase):

    def test_product_list_success(self):
        response = self.client.get('/ProductList/')
        self.assertEqual(response.status_code, 200)

class ProductDetailTestCase(TestCase):

    def test_product_detail_success(self):
        some_date = datetime(year=2024, month=12, day=25)
        dog1 = ProductCategory.objects.create(name='Умная собака')

        product = Product.objects.create(
            category=dog1,
            name="smart dog",
            price=1000000,
            sales_percent=None,
            description='Хорошая собака',
            new_expiry_date=some_date,
            preview_image='/media/dogs.jpg'
        )
        response = self.client.get(f'/ProductDetail/{product.id}/')

        self.assertEqual(response.status_code, 200)

    def test_product_detail_not_found(self):
        response = self.client.get('/ProductDetail/9999999999999999/')
        self.assertEqual(response.status_code, 404)

