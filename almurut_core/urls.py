from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from market.views import HomeView, FaqView, ErrorView, FavoritesView, LoginView, ProductDetailView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Home/', HomeView.as_view()),
    path('Faq/', FaqView.as_view()),
    path('Error/', ErrorView.as_view()),
    path('Favorites/', FavoritesView.as_view()),
    path('Login/', LoginView.as_view()),
    path('ProductDetail/', ProductDetailView.as_view())

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


