class animal:
    def __init__(self, nama, makanan, hidup, berkembang_biak):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak

    def cetak(self):
        print("Nama saya :", self.nama)
        print("Makanan saya :", self.makanan)
        print("Saya hidup di :", self.hidup)
        print("Saya berkembang biak dengan cara :", self.berkembang_biak)

class badak(animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, asal, kemampuan):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.asal = asal
        self.kemampuan = kemampuan

    def cetak(self):
        print("Nama saya :", self.nama)
        print("Makanan saya :", self.makanan)
        print("Saya hidup di :", self.hidup)
        print("Saya berkembang biak dengan cara :", self.berkembang_biak)
        print("Asal saya dari :", self.asal)
        print("Kemampuan saya :", self.kemampuan)

class Ikan(animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis, habitat):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis = jenis
        self.habitat = habitat

    def cetak(self):
        print("Nama saya :", self.nama)
        print("Makanan saya :", self.makanan)
        print("Saya hidup di :", self.hidup)
        print("Saya berkembang biak dengan cara :", self.berkembang_biak)
        print("Jenisnya :", self.jenis)
        print("Habitat saya di :", self.habitat)

class elang(animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna, berat):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna = warna
        self.berat = berat

    def cetak(self):
        print("Nama saya :", self.nama)
        print("Makanan saya :", self.makanan)
        print("Saya hidup di :", self.hidup)
        print("Saya berkembang biak dengan cara :", self.berkembang_biak)
        print("Warna saya adalah :", self.warna)
        print("Berat saya biasanya :", self.berat)

a = animal("Nama", "Makanan", "Hidup", "Berkembang biak")
a.cetak()

b = badak("Badak", "Buah dan Daun - daunan", "Darat", "Melahirkan", "Kalimantan", "Berlari hingga 64 km/jam")
b.cetak()

c = Ikan("Ikan", "Ikan kecil danInvertebrata", "Air tawar", "Bertelur", "Hiu", "Laut")
c.cetak()

d = elang("Elang", "Daging", "Wilayah perairan", "Bertelur", "Coklat dan Putih", "5 KG")
d.cetak()
