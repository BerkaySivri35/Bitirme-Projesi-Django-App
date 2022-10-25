from django.urls import path
from . import views
from .views import Proje_personel_ekle, Proje_hakem_ekle, Basvuru_kapak_ekle
urlpatterns = [
    path('', views.Home, name="Home"),
    path('basvuru-ekle/', Basvuru_kapak_ekle.as_view(), name="basvuru-ekle"),
    path('birinci-adim/', views.Basvuru_kapak, name="birinci-adim"),
    

    #İkinci Adımların url'leri
    path('ikinci-adim/', Proje_personel_ekle.as_view(), name="ikinci-adim"),
    path('ikinci-adim/proje-personel/', views.Proje_personeli ,name = 'proje-personel'),
    path('ikinci-adim/proje-personel/sil/<int:id>', views.Personel_Sil, name='sil'),
    path('ikinci-adim/proje-personel/duzenle/<int:id>', views.Personel_Update, name='duzenle'),
    path('ikinci-adim/proje-personel/duzenle/duzenle-personel/<int:id>', views.Personel_Duzenle_Kayit, name='duzenle-personel'),

    #Ucuncu adımın url'leri
    path('ucuncu-adim/', views.Belge_yukle, name = 'ucuncu-adim'),
    path('ucuncu-adim/belge-ekle/',views.KayitEkle, name= 'belge-ekle'),
    

    #Dorduncu adımın url'leri
    path('dorduncu-adim/',views.ProjeAlimlar, name= 'dorduncu-adim'),
    path('dorduncu-adim/proje-alimlar/', views.ProjeAlimKayit, name = 'proje-alimlar'),
    #Besinci adımın url'leri

    #Altinci adimin url'leri
    path('hakem-ekle/', Proje_hakem_ekle.as_view(), name = 'hakem-ekle'),
    path('altinci-adim/', views.Hakemler, name = 'altinci-adim'),
    path('altinci-adim/hakem-sil/<int:id>', views.Hakem_Sil, name='hakem-sil'),
    path('altinci-adim/hakem-duzenle/<int:id>', views.Hakem_Update, name='hakem-duzenle'),
    path('altinci-adim/hakem-duzenle/duzenle-kayit/<int:id>', views.Hakem_Duzenle_Kayit, name='duzenle-kayit'),
    
    #Yedinci adimin url'leri
    path('yedinci-adim/', views.Ek_yukle, name = 'yedinci-adim'),
    path('yedinci-adim/ek-dosyalar/', views.Proje_ek_dosya, name = 'ek-dosyalar'),
    
    #Sekizinci Adimin url'leri
    path('sekizinci-adim/', views.SonAdim, name = 'sekizinci-adim'),

]
