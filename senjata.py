import random

class Senjata:
    def __init__(self, nama: str, tipe_senjata: str, kekuatan: int, value: int) -> None:
        self.nama = nama
        self.tipe_senjata = tipe_senjata
        self.kekuatan = kekuatan
        self.value = value
    
    def damage(self):
        # Menghitung damage random
        damage_range = (self.kekuatan - self.kekuatan // 2, self.kekuatan + self.kekuatan // 2)
        damage = random.randint(*damage_range)
        return damage


tongkat_mage = Senjata(nama="Tongkat Mage", tipe_senjata="sihir", kekuatan=15, value=15)
busur_marksman = Senjata(nama="Busur Marksman", tipe_senjata="panah", kekuatan=20, value=12)
perisai_tanker = Senjata(nama="Perisai Tanker", tipe_senjata="pertahanan", kekuatan=10, value=20)

# Senjata untuk musuh
splash = Senjata(nama="Splash", tipe_senjata="air", kekuatan=10, value=8)
blackshadow = Senjata(nama="Blackshadow", tipe_senjata="kegelapan", kekuatan=15, value=15)