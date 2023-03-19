class Motor:
    def __init__(self, merk, warna):
        self.merk = merk
        self.warna = warna
    def info(self):
        print(f"Motor {self.merk} berwarna {self.warna}")


mobilA = Motor("Honda", "Putih")
mobilA.info() # Output: Mobil Toyota berwarna Hitam