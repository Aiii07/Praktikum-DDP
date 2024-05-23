class gempa:
    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala

    def dampak(self):
        if self.skala < 2:
            print("Dampak gempa di", self.lokasi, ": Tidak berasa")
        elif 2 <= self.skala < 4:
            print("Dampak gempa di", self.lokasi, ": Bangunan retak-retak")
        elif 4 <= self.skala < 6:
            print("Dampak gempa di", self.lokasi, ": Bangunan roboh")
        elif self.skala >= 6:
            print("Dampak gempa di", self.lokasi, ": Bangunan roboh dan berpotensi tsunami")