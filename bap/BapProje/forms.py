from attr import field, fields
from django import forms
from matplotlib import widgets
from . models import BasvuruKapak, ProjeHakemi, ProjePersoneli

class BasvuruKapakForm(forms.ModelForm):
    class Meta:
        model = BasvuruKapak
        fields = (
            'basvuran',
            'program_adi', 
            'projenin_turu', 
            'proje_basligi', 
            'anahtar_kelimeler', 
            'kurulus_adi', 
            'proje_baslamaTarihi', 
            'proje_suresi_Ay_cinsinden', 
            'proje_sahibi_cv', 
            )
        widgets = {
            'program_adi': forms.Select(attrs={'class':'form-control'}),
            'projenin_turu': forms.Select(attrs={'class':'form-control'}), 
            'basvuran': forms.TextInput(attrs={'class':'form-control','value':'', 'id':'kullanici_adi','type': 'hidden'}),
            'proje_basligi': forms.TextInput(attrs={'class':'form-control'}), 
            'anahtar_kelimeler' : forms.TextInput(attrs={'class':'form-control'}),
            'kurulus_adi': forms.TextInput(attrs={'class':'form-control'}),
            'proje_baslamaTarihi': forms.SelectDateWidget(attrs={'class':'form-control'}),
            'proje_suresi_Ay_cinsinden': forms.NumberInput(attrs={'class':'form-control'}),
            'proje_sahibi_cv': forms.FileInput(attrs={'class':'form-control'}),
            

        }    

class ProjePersoneliForm(forms.ModelForm):
    class Meta:
        model = ProjePersoneli
        fields = (
            'gorev',
            'unvan', 
            'basvuran', 
            'adi', 
            'soyadi', 
            'tc_no', 
            'universite', 
            'fakulte', 
            'bolum',
            'e_posta',
             'cv',
            )
        widgets = {
            'gorev': forms.Select(attrs={'class':'form-control'}),
            'unvan': forms.Select(attrs={'class':'form-control'}), 
            'basvuran': forms.TextInput(attrs={'class':'form-control','value':'', 'id':'kullanici_adi', 'type': 'hidden'}),
            'adi': forms.TextInput(attrs={'class':'form-control'}), 
            'soyadi' : forms.TextInput(attrs={'class':'form-control'}),
            'tc_no': forms.TextInput(attrs={'class':'form-control'}),
            'universite': forms.TextInput(attrs={'class':'form-control'}),
            'fakulte': forms.TextInput(attrs={'class':'form-control'}),
            'bolum': forms.TextInput(attrs={'class':'form-control'}),
            'e_posta': forms.EmailInput(attrs={'class':'form-control'}),
            'cv': forms.FileInput(attrs={'class':'form-control'}),
        }    

class ProjeHakemiForm(forms.ModelForm):
    class Meta:
        model = ProjeHakemi
        fields = (
            'unvan', 
            'basvuran', 
            'adi', 
            'soyadi', 
            'universite',  
            'fakulte', 
            'bolum',
            'e_posta',
            'telefon',
            'resim',
            )

        widgets = {
                'telefon': forms.TextInput(attrs={'class':'form-control'}),
                'unvan': forms.Select(attrs={'class':'form-control'}), 
                'basvuran': forms.TextInput(attrs={'class':'form-control','value':'', 'id':'kullanici_adi', 'type': 'hidden'}),
                'adi': forms.TextInput(attrs={'class':'form-control'}), 
                'soyadi' : forms.TextInput(attrs={'class':'form-control'}),
                'universite': forms.TextInput(attrs={'class':'form-control'}),
                'fakulte': forms.TextInput(attrs={'class':'form-control'}),
                'bolum': forms.TextInput(attrs={'class':'form-control'}),
                'e_posta': forms.EmailInput(attrs={'class':'form-control'}),
                'resim': forms.ClearableFileInput(attrs={'class':'form-control'}),
            }        