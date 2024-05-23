class orang:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def jalan(self):
        print("Saya Bisa Jalan")

    def cetak(self):
        print("Nama Saya", self.fname, self.lname)

class mahasiswa(orang):
    def __init__(self, fname, lname, prodi,angkatan):
        super().__init__(fname, lname)
        self.prodi = prodi
        self.angkatan = angkatan

    def print(self):
        print("Nama Saya", self.fname, self.lname)
        print("Prodi Saya", self.prodi)
        print("Saya Angkatan", self.angkatan)

class karyawan(orang):
    def __init__(self, fname, lname,jabatan):
        super().__init__(fname, lname)
        self.jabatan = jabatan

    def tampil(self):
        print("Nama Saya", self.fname, self.lname)
        print("Jabatan Saya", self.jabatan)

    

x = orang("Lee", "Mark")
x.cetak()
x.jalan()

y = mahasiswa("Lee", "Jisoo", "Teknik Informatika", "2023")
y.print()

aii = karyawan("Lee", "Do Hyun", "CEO")
aii.tampil()

