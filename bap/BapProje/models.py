from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

ProgramAdi_Choices = [
    ('FEN','FEN'),
    ('EDEBİYAT','EDEBİYAT'),
    ('İİBF','İİBF'),
    ('MÜHENDİSLİK','MÜHENDİSLİK'),
    ('MİMARLIK','MİMARLIK'),
]

ProjeninTuru_Choices = [
    ('KAP','Kapsamlı Araştırma Projeleri'),
    ('YP','Yönlendirilmiş Proje'),
    ('LÖAOPYÜKSEKLİSANS','LİSANSÜSTÜ ÖĞRENİM ARAŞTIRMA PROJELERİ (YÜKSEK LİSANS)'),
    ('LÖAOPDOKTORA','LİSANSÜSTÜ ÖĞRENİM ARAŞTIRMA PROJELERİ (DOKTORA)'),
    ('KAP2','Katılımlı Araştırma Projeleri'),
    ('AYP','ALT YAPI PROJELERİ'),
    ('KUS','Kamu-Üniversite-Sanayi İşbirliği Projeleri'),
    ('UUKP','Ulusal ve Uluslararası Kaynaklı Projeler'),
    ('HDP','Hızlı Destek Projeleri'),
]

Personel_gorev_Choices = [
    ('Araştırmacı','Araştırmacı'),
    ('Danışman','Danışman'),
    ('Bursiyer','Bursiyer'),
]
Unvan_Choices = [
    ('Prof. Dr.','Prof. Dr.'),
    ('Doç. Dr.','Doç. Dr.'),
    ('Yrd. Doç. Dr.','Yrd. Doç. Dr.'),
    ('Dr. Öğr. Üyesi','Dr. Öğr. Üyesi'),
    ('Uzm. Dr.','Uzm. Dr.'),
    ('Dr.','Dr.'),
    ('Uzm.','Uzm.'),
    ('Arş. Gör.','Arş. Gör.'),
    ('Arş. Gör. Dr.','Arş. Gör. Dr.'),
    ('Öğr. Gör. Dr.','Öğr. Gör. Dr.'),
    ('Öğr. Gör.','Öğr. Gör.'),
    ('Öğrenci','Öğrenci'),
    ('Yüksek Lisans Öğrencisi','Yüksek Lisans Öğrencisi'),
    ('Doktora Öğrencisi','Doktora Öğrencisi'),
    ('Diğer','Diğer'),
]

Yurtici_Yurtdisi_Choices = [
    ('Yurtiçi (Kongre / Sempozyum)','Yurtiçi (Kongre / Sempozyum)'),
    ('Yurtdışı (Kongre / Sempozyum)','Yurtdışı (Kongre / Sempozyum)'),
    ('Diğer','Diğer'),
]

#Adım 1 Tablo //
class BasvuruKapak(models.Model):
    program_adi = models.CharField(max_length=255,choices=ProgramAdi_Choices)
    projenin_turu = models.CharField(max_length=255,choices=ProjeninTuru_Choices)
    basvuran = models.ForeignKey(User, on_delete=models.CASCADE)
    proje_basligi = models.CharField(max_length=255) #label='Proje Özetinizi Buraya Yazınız.')
    anahtar_kelimeler = models.CharField(max_length=255) #label="Türkçe Anahtar Kelimeler")
    kurulus_adi = models.CharField(max_length=255) #label="Öneren/Projenin Yürütüleceği Kuruluşun Adı/ Yazışma Adresi")
    proje_baslamaTarihi = models.DateField()
    proje_suresi_Ay_cinsinden = models.IntegerField()
    proje_sahibi_cv = models.FileField(blank=True)

    def __str__(self):
        return self.program_adi + ' | ' + str(self.basvuran)
    
    def get_absolute_url(self):
        return reverse('birinci-adim')

#Adım 2 tablo //
class ProjePersoneli(models.Model):
    gorev = models.CharField(max_length=255, choices=Personel_gorev_Choices)
    unvan = models.CharField(max_length=255, choices=Unvan_Choices)
    basvuran = models.ForeignKey(User, on_delete=models.CASCADE)
    adi = models.CharField(max_length=50)
    soyadi = models.CharField(max_length=55)
    tc_no = models.CharField(max_length=11)
    universite = models.CharField(max_length=255)
    fakulte = models.CharField(max_length=255)
    bolum = models.CharField(max_length=255)
    e_posta = models.EmailField()
    cv = models.FileField(blank=True, upload_to="docs/")

    def __str__(self):
        return self.adi + ' | ' + str(self.basvuran)

    def get_absolute_url(self):
        return reverse('proje-personel')

#Adım 3 tablo //
class BelgeYukle(models.Model):
    Dosya = models.FileField(blank=True)
    basvuran_id = models.ForeignKey(User, null=True, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.Dosya) + ' | ' + str(self.basvuran)

#Adım 4 tablo //
class ProjeAlimlari(models.Model):
    basvuran_id = models.ForeignKey(User, null=True, default=1, on_delete=models.CASCADE)
    Malzeme_adi = models.CharField(max_length=200)
    Malzeme_Miktari = models.IntegerField()
    Malzeme_Fiyati = models.DecimalField(max_digits=10, decimal_places=2)
    Kullanim_Gerekceleri = models.TextField()
    Yurtici_Veya_Yurtdisi = models.CharField(max_length=100,choices=Yurtici_Yurtdisi_Choices)
    Hesaplamalar = models.TextField()
    Yolluklar_Miktari = models.IntegerField()
    Birim_Bedeli = models.DecimalField(max_digits=10, decimal_places=2)
    Yolluklar_Kullanim_Gerekceleri = models.TextField()
    Hizmet_Alimlari_Mahiyeti = models.CharField(max_length=200)
    Nereden_Kimden_Alinacagi = models.TextField()
    Hizmet_Alimlari_Miktar = models.IntegerField()
    Hizmet_Alimlari_Birim_Fiyati = models.DecimalField(max_digits=10, decimal_places=2)
    Hizmet_Alimlari_Kullanim_Gerekceleri = models.TextField()
    Menkul_Mal_Malzeme_Adi = models.CharField(max_length=250)
    Menkul_Mal_Miktar = models.IntegerField()
    Menkul_Mal_Birim_Fiyat = models.DecimalField(max_digits=10, decimal_places=2)
    Menkul_Mal_Kullanim_Gerekceleri = models.TextField()

    def __str__(self):
        return self.Malzeme_adi + ' | ' + str(self.basvuran)

#Adım 5 tablo //

#Adım 6 tablo //
class ProjeHakemi(models.Model):
    unvan = models.CharField(max_length=255, choices=Unvan_Choices)
    basvuran = models.ForeignKey(User, on_delete=models.CASCADE)
    adi = models.CharField(max_length=50)
    soyadi = models.CharField(max_length=55)
    universite = models.CharField(max_length=255)
    fakulte = models.CharField(max_length=255)
    bolum = models.CharField(max_length=255)
    e_posta = models.EmailField()
    telefon = models.CharField(max_length=11)
    resim = models.ImageField(blank = True, upload_to= "images/")

    def __str__(self):
        return self.adi + ' | ' + str(self.basvuran)
        
    def get_absolute_url(self):
        return reverse('altinci-adim')

#Adım 7 tablo //
class ProjeEkDosya(models.Model):
    basvuran_id = models.ForeignKey(User, null=True, default=1, on_delete=models.CASCADE)
    Dosya_Basligi = models.CharField(max_length=100)
    Aciklamasi = models.CharField(max_length=200)
    Dosya = models.FileField()

    def __str__(self):
        return self.Aciklamasi + ' | ' + str(self.basvuran)



# Create your models here.
