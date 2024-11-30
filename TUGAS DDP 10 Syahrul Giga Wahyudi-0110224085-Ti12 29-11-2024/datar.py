import math
# Fungsi untuk menghitung luas persegi
def luas_persegi(sisi):
    return sisi ** 2

# Fungsi untuk menghitung luas persegi panjang
def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

# Fungsi untuk menghitung luas segitiga
def luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

# Fungsi untuk menghitung luas lingkaran
def luas_lingkaran(jari_jari):
    return math.pi * jari_jari ** 2

# Fungsi untuk menghitung luas trapesium
def luas_trapesium(a, b, tinggi):
    return 0.5 * (a + b) * tinggi