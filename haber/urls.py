from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from .views import HaberListView, HaberDetailView, siyasat_sayfasi, ekonomiya_sayfasi, idman_sayfasi, texnologiya_sayfasi

urlpatterns = [
    path('', HaberListView.as_view(), name='haber_listesi'),
    path('haber/<int:pk>/', HaberDetailView.as_view(), name='haber_detay'),
    path('siyaset/', siyasat_sayfasi, name='siyaset_sayfasi'),  # Siyasət səhifəsi
    path('ekonomiya/', ekonomiya_sayfasi, name='ekonomiya_sayfasi'),
    path('idman/', idman_sayfasi, name='idman_sayfasi'),
    path('texnologiya/', texnologiya_sayfasi, name='texnologiya_sayfasi'),
    # siyaset_sayfasi URL-də qeyd edilir
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
