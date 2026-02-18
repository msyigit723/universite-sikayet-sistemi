from django.contrib import admin
from django.urls import path

# 1. ADIM: Fonksiyonları buraya çağırıyoruz (Import)
# tickets klasöründeki views dosyasından hem 'anasayfa'yı hem 'talep_olustur'u al diyoruz.
from tickets.views import anasayfa, talep_olustur 

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Anasayfa (Boş adres)
    path('', anasayfa, name='anasayfa'),

    # 2. ADIM: Yeni yolu (Path) buraya ekliyoruz
    # Adres çubuğuna 'yeni/' yazılınca 'talep_olustur' çalışsın.
    path('yeni/', talep_olustur, name='talep_olustur'),
]