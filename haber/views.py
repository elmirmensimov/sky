from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Haber
from .services import get_exchange_rate  # API fonksiyonunu doğru şekilde içe aktarıyoruz


# Siyaset Sayfası
def siyasat_sayfasi(request):
    # Burada "Siyasət" kateqoriyasını filtre edirsiniz.
    siyasat_haberler = Haber.objects.filter(kategori__isim="Siyasət").order_by('-yayinlanma_tarihi')
    return render(request, 'haber/siyaset.html', {'siyasat_haberler': siyasat_haberler})

# Siyaset Sayfası
def ekonomiya_sayfasi(request):
    # Burada "Siyasət" kateqoriyasını filtre edirsiniz.
    ekonomiya_haberler = Haber.objects.filter(kategori__isim="İqtisadiyyat").order_by('-yayinlanma_tarihi')
    return render(request, 'haber/ekonomiya.html', {'ekonomiya_haberler': ekonomiya_haberler})


def idman_sayfasi(request):
    # Burada "Siyasət" kateqoriyasını filtre edirsiniz.
    idman_haberler = Haber.objects.filter(kategori__isim="İdman").order_by('-yayinlanma_tarihi')
    return render(request, 'haber/idman.html', {'idman_haberler': idman_haberler})


def texnologiya_sayfasi(request):
    # Burada "Siyasət" kateqoriyasını filtre edirsiniz.
    texnologiya_haberler = Haber.objects.filter(kategori__isim="Texnologiya").order_by('-yayinlanma_tarihi')
    return render(request, 'haber/texnologiya.html', {'texnologiya_haberler': texnologiya_haberler})



# Haber Listesi Sayfası
class HaberListView(ListView):
    model = Haber
    template_name = 'haber/haber_listesi.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Popüler haberleri görüntülenme sayısına göre sıralıyoruz
        context['populer_haberler'] = Haber.objects.all().order_by('-gosterim_sayisi')[:7]

        # Kateqoriyalara göre haberleri filtreleyip ilgili kontekstlere yerleştiriyoruz
        context['gunun_one_cikanlar'] = Haber.objects.filter(kategori__isim="Günün Öne Çıkanları").order_by(
            '-yayinlanma_tarihi')[:5]
        context['manset_haberler'] = Haber.objects.filter(kategori__isim="Manşet").order_by('-yayinlanma_tarihi')[:3]
        context['en_son'] = Haber.objects.filter(kategori__isim="Ən son").order_by('-yayinlanma_tarihi')[:4]
        context['ekonomi_haberler'] = Haber.objects.filter(kategori__isim="İqtisadiyyat").order_by(
            '-yayinlanma_tarihi')[:4]
        context['spor_haberler'] = Haber.objects.filter(kategori__isim="İdman").order_by('-yayinlanma_tarihi')[:4]
        context['teknoloji_haberler'] = Haber.objects.filter(kategori__isim="Texnologiya").order_by(
            '-yayinlanma_tarihi')[:7]
        context['siyaset_haberler'] = Haber.objects.filter(kategori__isim="Siyasət").order_by('-yayinlanma_tarihi')[:10]

        return context


# Haber Detay Sayfası
class HaberDetailView(DetailView):
    model = Haber
    template_name = 'haber/haber_detayi.html'

    def get_object(self):
        haber = super().get_object()
        haber.gosterim_sayisi += 1  # Görüntülenme sayısını artırıyoruz
        haber.save()
        return haber
