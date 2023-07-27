class Hewan:

    def __init__(self, jenis):
        self.jenis = jenis

    def display_info(self):
        print(f"Jenis hewan: {self.jenis}")


class Mamalia(Hewan):
    def __init__(self, jenis, nama, makanan):
        super().__init__(jenis)
        self.nama = nama
        self.makanan = makanan

    def display_info(self):
        super().display_info()
        print(f"Nama mamalia: {self.nama}")
        print(f"Jenis Makanan: {self.makanan}")


class Singa(Mamalia):
    def __init__(self, jenis, nama, makanan):
        Mamalia.__init__(self, jenis, nama, makanan)

    def display_info(self):
        super().display_info()


# contoh penggunaan
singa = Singa("Mamalia", "Singa", "Daging")
singa.display_info()
