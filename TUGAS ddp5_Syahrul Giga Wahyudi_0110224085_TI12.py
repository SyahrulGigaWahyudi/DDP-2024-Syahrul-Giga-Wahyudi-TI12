#1
kendaraan = ['beat karbu','motor', 200, 'pink',2]

kendaraan.append('13jt')
kendaraan.append('matic')
kendaraan.insert (2, 'honda')
print(kendaraan)


# 2
hitung_luas = int(input("""pilih salahsatu :
1. hitung luas persegi
2. hitung luas lingkaran
3. hitung luas segitiga
"""))

match hitung_luas:
    case 1:
        print('menghitung luas persegi')
        sisi= float(input('masukan nilai sisi : '))
        hitung_luas_persegi=sisi**2
        print(f'jadi luas persegi dengan sisi {sisi} cm adalah {hitung_luas_persegi} cm^2')
    case 2:
        print('Menghitung luas lingkaran')
        jarijari=float(input('masukan nilai jari jari :'))
        hitung_luas_lingkaran=3.14*jarijari*jarijari
        print(f'jadi luas lingakaran dengan jari jari {jarijari}cm adalah {hitung_luas_lingkaran} cm^2')
    case 3:
        print('menghitung luas segitiga')
        alas=float(input('masukan nilai alas segitiga : '))
        tinggi=float(input('masukan nilai tinggi : '))
        luas=1/2*alas*tinggi
        print(f'jadi luas segitiga adalah {luas} cm^2')

    case _:
        print('pilihan tidak valid')
