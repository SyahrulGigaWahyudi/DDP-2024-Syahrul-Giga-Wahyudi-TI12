import math

def luas_kubus(sisi):
    """Menghitung luas permukaan kubus"""
    return 6 * (sisi ** 2)

def luas_balok(panjang, lebar, tinggi):
    """Menghitung luas permukaan balok"""
    return 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)

def luas_tabung(jari_jari, tinggi):
    """Menghitung luas permukaan tabung"""
    return 2 * math.pi * jari_jari * (jari_jari + tinggi)

def luas_kerucut(jari_jari, tinggi):
    """Menghitung luas permukaan kerucut"""
    selimut = math.sqrt(jari_jari**2 + tinggi**2)
    return math.pi * jari_jari * (jari_jari + selimut)

def luas_bola(jari_jari):
    """Menghitung luas permukaan bola"""
    return 4 * math.pi * (jari_jari ** 2)

def luas_prisma(alas, tinggi_alas, tinggi_prisma):
    """Menghitung luas permukaan prisma segitiga"""
    luas_alas = 2 * (0.5 * alas * tinggi_alas)
    luas_selimut = 3 * alas * tinggi_prisma
    return luas_alas + luas_selimut
