from django.shortcuts import render, redirect, get_object_or_404
from .models import Knihy, Uzivatele, Vypujcky

# 1. Hlavní katalog
def katalog(request):
    knihy = Knihy.objects.all()
    return render(request, 'core/index.html', {'knihy': knihy})

# 2. Detail knížky - OPRAVENO UKLÁDÁNÍ
def detail_knihy(request, kniha_id):
    kniha = get_object_or_404(Knihy, id=kniha_id)
    uzivatele = Uzivatele.objects.all()
    
    if request.method == "POST":
        jmeno_uzivatele = request.POST.get('uzivatel')
        
        # NAJDEME UŽIVATELE: Najde v databázi přesný objekt uživatele podle jména
        skutecny_uzivatel = get_object_or_404(Uzivatele, jmeno=jmeno_uzivatele)
        
        # ULOŽÍME VÝPŮJČKU: Teď už předáváme správný objekt, ne jen text
        Vypujcky.objects.create(
            kniha=kniha,
            uzivatel=skutecny_uzivatel
        )
        # Přesměruje na seznam všech výpůjček, kde se nová výpůjčka hned objeví
        return redirect('seznam_vypujcek')

    return render(request, 'core/detail.html', {'kniha': kniha, 'uzivatele': uzivatele})

# 3. Stránka se všemi půjčenými knihami
def seznam_vypujcek(request):
    vypujcky = Vypujcky.objects.all()
    return render(request, 'core/vypujcka.html', {'vypujcky': vypujcky})