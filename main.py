class Hayvon:
    def __init__(self, turi):
        self.turi = turi
        self.ovoz = ""
    
    def ovoz_chiqar(self):
        print(f"{self.turi}: {self.ovoz}")

class Kuchuk(Hayvon):
    def __init__(self, nomi):
        super().__init__("Kuchuk")
        self.nomi = nomi
        self.ovoz = "Woof! Woof!"

class Mushuk(Hayvon):
    def __init__(self, nomi):
        super().__init__("Mushuk")
        self.nomi = nomi
        self.ovoz = "Meow! Meow!"

# Test
kuchuk = Kuchuk("Rex")
mushuk = Mushuk("Mimi")

kuchuk.ovoz_chiqar()
mushuk.ovoz_chiqar()
