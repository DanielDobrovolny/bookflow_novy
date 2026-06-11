from django.db.models import Model, CharField, DateTimeField, IntegerField, ForeignKey, CASCADE

class Uzivatele(Model):
    jmeno = CharField(max_length=100)
    email = CharField(unique=True, max_length=100)
    heslo = CharField(max_length=255)
    datum_registrace = DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uzivatele'

    def __str__(self):
        return self.jmeno


class Knihy(Model):
    nazev = CharField(max_length=255)
    autor = CharField(max_length=100)
    isbn = CharField(unique=True, max_length=20)
    rok_vydani = IntegerField()
    dostupna = IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'knihy'

    def __str__(self):
        return f"{self.nazev} ({self.autor})"


class Vypujcky(Model):
    uzivatel = ForeignKey(Uzivatele, CASCADE)
    kniha = ForeignKey(Knihy, CASCADE)
    datum_vypujceni = DateTimeField(blank=True, null=True)
    datum_vraceni = DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vypujcky'

    def __str__(self):
        return f"{self.uzivatel.jmeno} -> {self.kniha.nazev}"