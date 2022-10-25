# Generated by Django 4.0.3 on 2022-06-28 14:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('BapProje', '0010_basvurukapak_basvuran_belgeyukle_basvuran_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjeAlimlari',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Malzeme_adi', models.CharField(max_length=200)),
                ('Malzeme_Miktari', models.IntegerField()),
                ('Malzeme_Fiyati', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Kullanim_Gerekceleri', models.TextField()),
                ('Yurtici_Veya_Yurtdisi', models.CharField(choices=[('Yurtiçi (Kongre / Sempozyum)', 'Yurtiçi (Kongre / Sempozyum)'), ('Yurtdışı (Kongre / Sempozyum)', 'Yurtdışı (Kongre / Sempozyum)'), ('Diğer', 'Diğer')], max_length=100)),
                ('Hesaplamalar', models.TextField()),
                ('Yolluklar_Miktari', models.IntegerField()),
                ('Birim_Bedeli', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Yolluklar_Kullanim_Gerekceleri', models.TextField()),
                ('Hizmet_Alimlari_Mahiyeti', models.CharField(max_length=200)),
                ('Nereden_Kimden_Alinacagi', models.TextField()),
                ('Hizmet_Alimlari_Miktar', models.IntegerField()),
                ('Hizmet_Alimlari_Birim_Fiyati', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Hizmet_Alimlari_Kullanim_Gerekceleri', models.TextField()),
                ('Menkul_Mal_Malzeme_Adi', models.CharField(max_length=250)),
                ('Menkul_Mal_Miktar', models.IntegerField()),
                ('Menkul_Mal_Birim_Fiyat', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Menkul_Mal_Kullanim_Gerekceleri', models.TextField()),
                ('basvuran', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]