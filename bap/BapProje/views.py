from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from matplotlib.style import context
from .models import BasvuruKapak, ProjeAlimlari, ProjeEkDosya, ProjeHakemi, ProjePersoneli, BelgeYukle
from django.views.generic import CreateView
from django.template import loader
from .forms import BasvuruKapakForm, ProjePersoneliForm, ProjeHakemiForm
def Home(request):
    return render(request, 'Home.html', {})
#1.Adım //
def Basvuru_kapak(request):
    kapak_sayfasi = BasvuruKapak.objects.all().values()
    template = loader.get_template('basvuru_kapak.html')
    context = {
        'kapak_sayfasi': kapak_sayfasi,
    }
    return HttpResponse(template.render(context,request))

class Basvuru_kapak_ekle(CreateView):
    model = BasvuruKapak
    form_class = BasvuruKapakForm
    template_name = 'birinci_adim.html'
    #fields = '__all__'
       

#2.Adım //
def Proje_personeli(request):
    personel_sayfasi = ProjePersoneli.objects.all().values()
    template = loader.get_template('proje_personel.html')
    context = {
        'personel_sayfasi': personel_sayfasi,
    }
    return HttpResponse(template.render(context,request))

class Proje_personel_ekle(CreateView):
    model = ProjePersoneli
    form_class = ProjePersoneliForm
    template_name = 'ikinci_adim.html'
    #fields = '__all__'

def Personel_Sil(request, id):
  personel = ProjePersoneli.objects.get(id=id)
  personel.delete()
  return HttpResponseRedirect(reverse('proje-personel'))

def Personel_Update(request, id):
  personel_duzenle = ProjePersoneli.objects.get(id=id)
  template = loader.get_template('personel_duzenle.html')
  context = {
    'personel_duzenle': personel_duzenle,
  }
  return HttpResponse(template.render(context, request))

def Personel_Duzenle_Kayit(request, id):
  a = request.POST['adi']
  b = request.POST['soyad']
  c = request.POST['uni']
  d = request.POST['fakulte']
  e = request.POST['bolum']
  f = request.POST['eposta']
  g = request.POST['cv']
  
  personel = ProjePersoneli.objects.get(id=id)
  personel.adi = a
  personel.soyadi = b
  personel.universite = c
  personel.fakulte = d
  personel.bolum = e
  personel.e_posta = f
  personel.cv = g
  personel.save()
  return HttpResponseRedirect(reverse('proje-personel'))

#3.Adım //
def Belge_yukle(request):
    template = loader.get_template('ucuncu_adim.html')
    return HttpResponse(template.render({},request))

def KayitEkle(request):
    x = request.POST['Dosya']
    FILE = BelgeYukle(Dosya = x)
    FILE.save()
    return HttpResponseRedirect(reverse('dorduncu-adim'))




# 4.Adım //
def ProjeAlimlar(request):
    projeAlim_Sayfasi = ProjeAlimlari.objects.all().values()
    template = loader.get_template('dorduncu_adim.html')
    context ={
    'projeAlim_Sayfasi': projeAlim_Sayfasi,
    }
    return HttpResponse(template.render(context,request))

def ProjeAlimKayit(request):

    #a = request.POST['basvuran_id']
    b = request.POST['malzemeAdi']
    c = request.POST['malzemeMiktari']
    d = request.POST['malzemeFiyati']
    e = request.POST['kullanimGerekce']
    f = request.POST['yurticiYurtdisi']
    g = request.POST['hesaplamalar']
    h = request.POST['yollukMiktar']
    j = request.POST['birimBedel']
    k = request.POST['yollukKullanimGerekce']
    l = request.POST['hizmetMahiyet']
    m = request.POST['nerdenKimden']
    n = request.POST['hizmetMiktar']
    o = request.POST['hizmetBirimFiyat']
    p = request.POST['hizmetGerekce']
    r = request.POST['menkulAdi']
    s = request.POST['menkulMiktar']
    t = request.POST['menkulFiyat']
    v = request.POST['menkulGerekce']
    
    kaydet = ProjeAlimlari(
        #basvuran_id = a,
        Malzeme_adi = b,
        Malzeme_Miktari = c,
        Malzeme_Fiyati = float(d),
        Kullanim_Gerekceleri = e,
        Yurtici_Veya_Yurtdisi = f,
        Hesaplamalar = g,
        Yolluklar_Miktari = h,
        Birim_Bedeli = float(j),
        Yolluklar_Kullanim_Gerekceleri = k,
        Hizmet_Alimlari_Mahiyeti = l,
        Nereden_Kimden_Alinacagi = m,
        Hizmet_Alimlari_Miktar = n,
        Hizmet_Alimlari_Birim_Fiyati = float(o),
        Hizmet_Alimlari_Kullanim_Gerekceleri = p,
        Menkul_Mal_Malzeme_Adi = r,
        Menkul_Mal_Miktar = s,
        Menkul_Mal_Birim_Fiyat = float(t),
        Menkul_Mal_Kullanim_Gerekceleri = v,
    )
    kaydet.save()

    return HttpResponseRedirect(reverse('dorduncu-adim'))


#6.Adım //
class Proje_hakem_ekle(CreateView):
    model = ProjeHakemi
    form_class = ProjeHakemiForm
    template_name = 'hakem_ekle.html'
    #fields = '__all__'

def Hakemler(request):
    hakem_sayfasi = ProjeHakemi.objects.all().values()
    template = loader.get_template('altinci_adim.html')
    context = {
        'hakem_sayfasi': hakem_sayfasi,
    }
    return HttpResponse(template.render(context,request))

def Hakem_Sil(request, id):
  hakem = ProjeHakemi.objects.get(id=id)
  hakem.delete()
  return HttpResponseRedirect(reverse('altinci-adim'))

def Hakem_Update(request, id):
  hakem_duzenle = ProjeHakemi.objects.get(id=id)
  template = loader.get_template('hakem_duzenle.html')
  context = {
    'hakem_duzenle': hakem_duzenle,
  }
  return HttpResponse(template.render(context, request))

def Hakem_Duzenle_Kayit(request, id):
  first = request.POST['first']
  last = request.POST['last']
  soyad = request.POST['soyad']
  uni = request.POST['uni']
  fakulte = request.POST['fakulte']
  bolum = request.POST['bolum']
  posta =request.POST['posta']
  tel = request.POST['tel']
  hakem = ProjeHakemi.objects.get(id=id)
  hakem.adi = first
  hakem.unvan = last
  hakem.soyadi = soyad
  hakem.universite = uni
  hakem.fakulte = fakulte
  hakem.bolum = bolum
  hakem.e_posta = posta
  hakem.telefon = tel
  hakem.save()
  return HttpResponseRedirect(reverse('altinci-adim'))       

#7.Adım //
def Ek_yukle(request):
    proje_ekDosya = ProjeEkDosya.objects.all().values()
    template = loader.get_template('yedinci_adim.html')
    context = {
        'proje_ekDosya': proje_ekDosya,
    }
    return HttpResponse(template.render(context,request))

def Proje_ek_dosya(request):
    #a = request.POST['basvuran_id']
    x = request.POST['baslik']
    y = request.POST['aciklama']
    z = request.POST['dosya']
    file = ProjeEkDosya(
        #basvuran_id = a,
        Dosya_Basligi = x, 
        Aciklamasi = y, 
        Dosya = z )
    file.save()
    #proje_ekDosya = ProjeEkDosya.objects.all().values()
    #
    #context = {
    #    'proje_ekDosya': proje_ekDosya,
    #}
    return HttpResponseRedirect(reverse('yedinci-adim'))
    #return HttpResponse(template.render(context,request))

# 8.Adım //
def SonAdim(request):
    template = loader.get_template('sekizinci_adim.html')
    return HttpResponse(template.render({},request))

    #proje_ekDosya = ProjeEkDosya.objects.all().values()
    #template = loader.get_template('yedinci_adim.html')
    #context = {
    #    'proje_ekDosya': proje_ekDosya,
    #}
    #return HttpResponse(template.render(context,request))       

# Create your views here.
