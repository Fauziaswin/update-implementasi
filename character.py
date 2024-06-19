from bar_kesehatan import KesehatanBar
import random

class Character:
    def __init__(self, nama: str, kesehatan: int, senjata) -> None:
        self.nama = nama
        self.kesehatan = kesehatan
        self.kesehatan_max = kesehatan
        self.senjata = senjata
    
    def serangan(self, target):
        # Menghitung damage
        damage = self.senjata.damage()

        # Cek kritikal hit
        is_critical = random.random() < 0.2  # 20% kemungkinan kritikal hit
        if is_critical:
            damage *= 2  # Menggandakan damage untuk kritikal hit
            print(f"⚔️, {self.nama} Kritikal {target.nama} dengan {self.senjata.nama}, menyebabkan {damage} kerusakan! ☠️ ")
        else:
            print(f"⚔️, {self.nama} menyerang {target.nama} dengan {self.senjata.nama}, menyebabkan {damage} kerusakan! ☠️ ")

        # Mengurangi kesehatan target
        target.kesehatan -= damage
        target.kesehatan = max(target.kesehatan, 0)
        target.bar_kesehatan.update()
        
class pahlawan(Character):
    def __init__(self, nama: str, kesehatan: int, senjata) -> None:
        super().__init__(nama, kesehatan, senjata)
        self.default_senjata = self.senjata
        self.bar_kesehatan = KesehatanBar(self, color="green")
    
    def equip(self, senjata) -> None:
        self.senjata = senjata
        print(f"{self.nama} menggunakan {self.senjata.nama}!")
    
    def drop(self) -> None:
        print(f"{self.nama} menurunkan {self.senjata.nama}!")
        self.senjata = self.default_senjata
        
class Musuh(Character):
    def __init__(self, nama: str, kesehatan: int, senjata) -> None:
        super().__init__(nama, kesehatan, senjata)
        self.bar_kesehatan = KesehatanBar(self, color="red")
