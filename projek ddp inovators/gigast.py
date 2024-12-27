import streamlit as st
import locale

# Atur locale untuk Indonesia
locale.setlocale(locale.LC_ALL, 'id_ID.UTF-8')

def parse_rupiah(input_rupiah):
    """
    Mengonversi string format Rp (contoh: '10,000,000') menjadi angka float.
    """
    return float(input_rupiah.replace('Rp', '').replace('.', '').replace(',', '').strip())


st.title("kalkulator cicilan bulanan")

#input pinjaman
jumlah_pinjaman =st.text_input("masukan jumlah pinjaman (RP)",0)
jumlah_pinjaman = parse_rupiah(jumlah_pinjaman)
    
#input suku bungan tahunan
suku_bunga_tahunan=st.number_input("masukan suku bunga tahunan(%)",min_value=0.0)
#Input lama pinjaman dalam bulan
lama_pinjaman=st.number_input("masukan lama pinjaman (bulan)",0)
if st.button("HITUNG"):
    if jumlah_pinjaman >0 and suku_bunga_tahunan >0 and lama_pinjaman >0: 
        #hitung suku bunga
        suku_bunga_bulanan = suku_bunga_tahunan / 12 / 100
        # Hitung cicilan bulanan menggunakan rumus anuitas
        cicilan_bulanan= (jumlah_pinjaman*suku_bunga_bulanan)/ (1- (1+suku_bunga_bulanan)**(- lama_pinjaman))
        #total yang di bayarkan
        total=cicilan_bulanan * lama_pinjaman
         #total bunga yang di bayarkan
        total_bunga=total - jumlah_pinjaman

   

        #hasil
        st.header("Hasil Inputan")
        st.write(f"jumlah pinjaman: {locale.currency(jumlah_pinjaman,grouping=True)}")  
        st.write(f"suku bunga tahunan: {suku_bunga_tahunan}%")
        st.write(f"lama pinjaman: {lama_pinjaman} Bulan")
        st.header("Hasil perhitungan Cicilan Bulanan")
        st.write(f"cicilan bulanan: {locale.currency(cicilan_bulanan,grouping=True)}")
        st.write(f"total pinjaman yang di bayarkan: {locale.currency(total,grouping=True)}")
        st.write(f"total bunga yang di bayarkan: {locale.currency(total_bunga,grouping=True)}")
        st.success(f"CICILAN YANG HARUS DI BAYAR KAN SETIAP BULAN: {locale.currency(cicilan_bulanan,grouping=True)}")
        
    else:   
        st.warning("Masukkan nilai yang valid untuk semua input.")
else:
    st.warning("Tekan tombol **Hitung Cicilan** setelah mengisi input.")
