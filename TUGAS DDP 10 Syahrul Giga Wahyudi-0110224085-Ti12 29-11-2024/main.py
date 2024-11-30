from hitungg import*

def hitung_aritmatika():
    print("\n=== MENU OPERASI ARITMATIKA===")
    print("1.Tambah")
    print("2.Kurang")
    print("3.kali")
    print("4.Bagi")
    print("5.Pangkat")
    pilihan=int(input("\n===Masukan  nomor operasi aritmatika yang di pilih (1-5)===: "))
    if pilihan==1:
        a=float(input("Masukan angka pertama:"))
        b=float(input("Masukan angka kedua:"))
        print("\n=== Hasil Penambahan === :",tambah(a,b))
    elif pilihan==2:
        a=float(input("Masukan Angka Pertama:"))
        b=float(input("Masukan Angka Kedua:"))
        print("\n=== Hasil Pengurangan === :",kurang(a,b))
    elif pilihan==3:
        a=float(input("Masukan Angka Pertama:"))
        b=float(input("Masukan Angka Kedua:"))
        print("\===Hasil Perkalian=== :",kali(a,b))
    elif pilihan==4:
        a=float(input("Masukan Angka Pertama:"))
        b=float(input("Masukan Angka Kedua:"))
        print("\n===Hasil Pembagian=== :",bagi(a,b))
    elif pilihan==5:
        a=float(input("Masukan Angka Pertama:"))
        b=float(input("Masukan Angka Kedua:"))
        print("\n===Hasil Pangkat=== :",pangkat(a,b))
    else:
        print("pilihan tidak Valid")

from datar import*

def hitung_luas_bangun_datar():
    print("\n=== MENU OPERASI LUAS BANGUN DATAR ===")
    print("1.Luas Persegi")
    print("2.Luas Persegi Panjang ")
    print("3.Luas Segitiga")
    print("4.Luas Lingkaran")
    print("5.Trapesium")

    pilihan=int(input("\n=== MENU LUAS BANGUN DATAR (1-5)===:"))
    if pilihan==1:
        sisi=float(input("Masukan Nilai Sisi:"))
        print("\n===Hasil Luas Persegi === :",luas_persegi(sisi))
    elif pilihan==2:
        panjang=float(input("Masukan Nilai Panjang:"))
        lebar=float(input("Masukan Nilai Lebar:"))
        print("\n=== Hasil Luas Persegi Panjang === :",luas_persegi_panjang(panjang,lebar))
    elif pilihan==3:
        alas=float(input("Masukan Nilai Alas:"))
        tinggi=float(input("Masukan Nilai Tinggi:"))
        print("\n===Hasil Luas Segitiga === :",luas_segitiga(alas,tinggi))
    elif pilihan==4:
        jari_jari=float(input("Masukan  Nilai jari-jari:"))
        print("\n=== Hasil Luas Lingkaran === ",luas_lingkaran(jari_jari))
    elif pilihan==5:
        a=float(input("Masukan Nilai sisi A:"))
        b=float(input("Masukan Nilai sisi B:"))
        tinggi=float(input("Masukan Nilai tinggi:"))
        print("\n=== Hasil Luas Trapesium === :",luas_trapesium(a,b,tinggi))
    else:
        print("pilihan tidak Valid")


from ruang import*
def hitung_luas_bangun_ruang():
    print("\n=== MENU OPERASI LUAS PERMUKAAN BANGUN RUANG ===")
    print("1.Luas Kubus")
    print("2.Luas Balok")
    print("3.Luas Tabung")
    print("4.Luas Kerucut")
    print("5.Luas Bola")
    pilihan=int(input("\n===Masukan  nomor operasi luas bangun RUANG yang di pilih (1-5)===:"))
    if pilihan==1:
        sisi=float(input("masukan nilai sisi:"))
        print("\n=== Luas Permukaan Kubus=== :",luas_kubus(sisi))
    elif pilihan==2:
        panjang=float(input("Masukan Panjang Balok:"))
        lebar=float(input("Masukan Lebar Balok:"))
        tinggi=float(input("Masukan Tinggi Balok:"))
        print("\n=== Luas permukaan balok === :",luas_balok(panjang,lebar,tinggi))
    elif pilihan==3:
        jari_jari=float(input("Masukan Nilai jari-jari:"))
        tinggi=float(input("Masukan Nilai Tinggi: "))
        print("\n=== Luas Permukaan Tabung=== :",luas_tabung(jari_jari,tinggi))
    elif pilihan==4:
        jari_jari=float(input("Masukan Nilai jari-jari:"))
        tinggi=float(input("masukan nilai tinggi: "))
        print("\n=== luas Permukaan Kerucut=== :",luas_kerucut(jari_jari,tinggi))
    elif pilihan==5:
        jari_jari=float(input("masukan nilai jari jari:"))
        print("\n=== Luas Permukaan Bola === :",luas_bola(jari_jari))

def tampilkan_menu():
    print("\n=== MENU UTAMA ===")
    print("dibuat oleh Syahrul Giga Wahyudi")
    print("1. Hitung Operasi Aritmatika")
    print("2. Hitung Luas Bangun Datar")
    print("3. Hitung Luas Bangun Ruang")
    print("4. Keluar")

def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-4): ")
        if pilihan == "1":
            hitung_aritmatika()
        elif pilihan == "2":
            hitung_luas_bangun_datar()
        elif pilihan == "3":
            hitung_luas_bangun_ruang()
        elif pilihan == "4":
            print("Keluar dari program. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Jalankan program utama
if __name__ == "__main__":
    main()