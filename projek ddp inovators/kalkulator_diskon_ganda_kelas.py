class DiskonGanda:
    def __init__(self, harga_awal, diskon_pertama, diskon_kedua):
        self.harga_awal = harga_awal
        self.diskon_pertama = diskon_pertama
        self.diskon_kedua = diskon_kedua

    def harga_setelah_diskon_pertama(self):
        # Menghitung harga setelah diskon pertama
        harga_pertama = self.harga_awal * (1 - self.diskon_pertama / 100)
        diskon_pertama = self.harga_awal - harga_pertama  # Menghitung jumlah diskon
        return harga_pertama, diskon_pertama

    def harga_setelah_diskon_kedua(self):
        # Menghitung harga setelah diskon kedua (tanpa diskon pertama)
        harga_kedua = self.harga_awal * (1 - self.diskon_kedua / 100)
        diskon_kedua = self.harga_awal - harga_kedua  # Menghitung jumlah diskon
        return harga_kedua, diskon_kedua

    def harga_akhir(self):
        # Menghitung diskon gabungan dengan cara yang lebih sesuai
        diskon_pertama = self.harga_awal * (self.diskon_pertama / 100)
        diskon_kedua = self.harga_awal * (self.diskon_kedua / 100)
        
        total_diskon = diskon_pertama + diskon_kedua  # Gabungkan kedua diskon
        harga_akhir = self.harga_awal - total_diskon  # Harga akhir setelah kedua diskon digabung
        
        return harga_akhir, total_diskon