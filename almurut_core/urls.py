from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from market.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Home/', HomeView.as_view())

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


