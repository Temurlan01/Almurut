from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from market.views import HomeView, FaqView, ErrorView, FavoritesView, \
     ProductDetailView, ProductListView, ShoppingCartView

from users.views import UserRegisterView, UserMakeRegisterView, \
    UserLoginView, UserMakeLoginView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Home/', HomeView.as_view(), name='Home-url'),
    path('Faq/', FaqView.as_view(), name='Faq-url'),
    path('Error/', ErrorView.as_view()),
    path('Favorites/', FavoritesView.as_view()),
    path('login/', UserLoginView.as_view()),
    path('ProductDetail/', ProductDetailView.as_view()),
    path('ProductList/', ProductListView.as_view(), name='Shop-url'),
    path('ShoppingCart/', ShoppingCartView.as_view()),
    path('registration/', UserRegisterView.as_view(), name='registration-url'),
    path('make-registration/', UserMakeRegisterView.as_view(), name='make-registration-url'),
    path('make-login/', UserMakeLoginView.as_view(), name='make-login-url')

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


