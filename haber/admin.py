from django.contrib import admin
from .models import Kategori, Haber

@admin.register(Kategori)
class KategoriAdmin(admin.ModelAdmin):
    list_display = ('isim',)

@admin.register(Haber)
class HaberAdmin(admin.ModelAdmin):
    list_display = ('baslik', 'kategori', 'yayinlanma_tarihi', 'yazar', 'on_bilgi')  # Ön bilgi sahəsini əlavə etdik
    list_filter = ('kategori', 'yayinlanma_tarihi')
    search_fields = ('baslik', 'icerik', 'on_bilgi')  # Ön bilgi sahəsini axtarış sahələrinə əlavə etdik
