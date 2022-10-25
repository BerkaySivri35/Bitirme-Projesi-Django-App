from django.contrib import admin
from . models import BasvuruKapak, ProjeAlimlari, ProjePersoneli, BelgeYukle, ProjeHakemi, ProjeEkDosya
# Register your models here.
admin.site.register(BasvuruKapak),
admin.site.register(ProjePersoneli),
admin.site.register(BelgeYukle),
admin.site.register(ProjeHakemi),
admin.site.register(ProjeEkDosya),
admin.site.register(ProjeAlimlari),
