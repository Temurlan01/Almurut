from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models

from users.models import CustomUser


class ProductCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = 'Категория товаров'
        verbose_name = 'Категория товара'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField(verbose_name='цена без скидки', help_text='в сомах')
    sales_percent = models.PositiveSmallIntegerField(
        verbose_name='скидка в процентах',
        null=True,
        validators=[MaxValueValidator(100)],
        blank=True,
        )
    description = models.TextField()
    preview_image = models.ImageField(upload_to='products_preview_images/')
    new_expiry_date = models.DateField()

    class Meta:
        verbose_name_plural = 'Товары'
        verbose_name = 'Товар'

    def get_price_with_sales(self):

        if self.sales_percent == 0 or self.sales_percent == None:
            return self.price
        else:
            return int((self.price / 100) * (100 - self.sales_percent))

    def __str__(self):
        return self.name


class ProductGallery(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='gallery')
    image = models.ImageField(upload_to='product_gallery/')

    class Meta:
        verbose_name_plural = 'Галерея товаров'
        verbose_name = 'Галерея товара'


class ProductRating(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])