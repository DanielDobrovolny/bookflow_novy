from django.shortcuts import render
from .models import Knihy  # Importujeme tvůj model knih

def hlavni_stranka(request):
    # Vytáhneme všechny knihy z databáze
    vsechny_knihy = Knihy.objects.all()
    
    # Pošleme je do HTML šablony
    return render(request, 'core/index.html', {'knihy': vsechny_knihy})