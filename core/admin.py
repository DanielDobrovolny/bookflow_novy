from django.contrib import admin
from .models import Uzivatele, Knihy, Vypujcky

@admin.register(Uzivatele)
class UzivateleAdmin(admin.ModelAdmin):
    list_display = ('id', 'jmeno', 'email', 'datum_registrace')
    search_fields = ('jmeno', 'email')

@admin.register(Knihy)
class KnihyAdmin(admin.ModelAdmin):
    list_display = ('id', 'nazev', 'autor', 'isbn', 'rok_vydani', 'dostupna')
    list_filter = ('dostupna', 'autor')
    search_fields = ('nazev', 'autor')

@admin.register(Vypujcky)
class VypujckyAdmin(admin.ModelAdmin):
    # Odsud jsme smazali 'datum_vypujceni' a 'datum_vraceni', protože v modelech nejsou!
    list_display = ('id', 'uzivatel', 'kniha')