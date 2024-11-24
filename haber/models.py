from django.db import models

class Kategori(models.Model):
    isim = models.CharField(max_length=100)

    def __str__(self):
        return self.isim

class Haber(models.Model):
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE, related_name='haberler')
    baslik = models.CharField(max_length=200)
    on_bilgi = models.CharField(max_length=300, blank=True, null=True)  # Yeni ön bilgi alanı
    icerik = models.TextField()
    yayinlanma_tarihi = models.DateTimeField(auto_now_add=True)
    yazar = models.CharField(max_length=100)
    resim = models.ImageField(upload_to='haber_resimleri/', blank=True, null=True)
    gosterim_sayisi = models.IntegerField(default=0)  # Görüntülenme sayısı alanı



    def __str__(self):
        return self.baslik
