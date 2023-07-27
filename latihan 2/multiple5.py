class Person:

    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def display_info(self):
        print(f"Nama: {self.nama}")
        print(f"Umur: {self.umur}")


class Mahasiswa(Person):

    def __init__(self, nama, umur, jurusan, tahun_lulus):
        super().__init__(nama, umur)
        self.jurusan = jurusan
        self.tahun_lulus = tahun_lulus

    def display_info(self):
        super().display_info()
        print(f"Jurusan: {self.jurusan}")


class MahasiswaAlumni(Mahasiswa):

    def __init__(self, nama, umur, jurusan, tahun_lulus):
        Mahasiswa.__init__(self, nama, umur, jurusan, tahun_lulus)

    def display_info(self):
        super().display_info()
        print(f"Tahun lulus: {self.tahun_lulus}")


# contoh penggunaan
mahasiswa_alumniA = MahasiswaAlumni("Budi", 20, "Informatika", 2022)
mahasiswa_alumniA.display_info()
