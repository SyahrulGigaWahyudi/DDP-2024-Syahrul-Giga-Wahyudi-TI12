import streamlit as st
import locale
from kalkulator_diskon_ganda_kelas import *

# Mengatur locale ke Indonesia agar format rupiah sesuai
locale.setlocale(locale.LC_ALL, 'id_ID.UTF-8')

# Judul halaman
st.title("Perhitungan Diskon Ganda")

# Input harga awal barang dan persentase diskon
harga_awal = st.number_input("Masukkan harga barang (dalam Rupiah):", min_value=0.0, step=1000.0)
diskon_pertama = st.number_input("Masukkan diskon pertama (%):", min_value=0.0, max_value=100.0, step=0.1)
diskon_kedua = st.number_input("Masukkan diskon kedua (%):", min_value=0.0, max_value=100.0, step=0.1)

# Membuat objek diskon
diskon = DiskonGanda(harga_awal, diskon_pertama, diskon_kedua)

# Menampilkan pilihan hasil diskon
st.subheader("Pilih jenis perhitungan diskon yang ingin ditampilkan:")

option = st.radio("Pilih jenis diskon", ("Diskon Pertama", "Diskon Kedua", "Diskon Gabungan"))

if option == "Diskon Pertama":
    harga_pertama, diskon_pertama_total = diskon.harga_setelah_diskon_pertama()
    st.write(f"Harga setelah diskon pertama ({diskon_pertama}%): {locale.currency(harga_pertama, grouping=True)}")
    st.write(f"Diskon yang diterima: {locale.currency(diskon_pertama_total, grouping=True)}")
    st.success(f"Anda menghemat total: {locale.currency(diskon_pertama_total, grouping=True)}")

elif option == "Diskon Kedua":
    harga_kedua, diskon_kedua_total = diskon.harga_setelah_diskon_kedua()
    st.write(f"Harga setelah diskon kedua ({diskon_kedua}%): {locale.currency(harga_kedua, grouping=True)}")
    st.write(f"Diskon yang diterima: {locale.currency(diskon_kedua_total, grouping=True)}")
    st.success(f"Anda menghemat total: {locale.currency(diskon_kedua_total, grouping=True)}")

elif option == "Diskon Gabungan":
    harga_akhir, diskon_total = diskon.harga_akhir()
    st.write(f"Harga akhir setelah kedua diskon digabung: {locale.currency(harga_akhir, grouping=True)}")
    st.write(f"Total diskon yang diterima: {locale.currency(diskon_total, grouping=True)}")
    st.success(f"Anda menghemat total: {locale.currency(diskon_total, grouping=True)}")
