import streamlit as st
import locale

# Atur locale untuk Indonesia
locale.setlocale(locale.LC_ALL, 'id_ID.UTF-8')

def parse_rupiah(input_rupiah):
    """
    Mengonversi string format Rp (contoh: '10,000,000') menjadi angka float.
    """
    return float(input_rupiah.replace('Rp', '').replace('.', '').replace(',', '').strip())


# Title
st.title("Kalkulator Tabungan Target")

# Input fields
target_keuangan = st.text_input("Masukkan target keuangan atau nominal yang ingin dicapai:",0)
target_keuangan= parse_rupiah(target_keuangan)

durasi_hari = st.number_input("Masukkan durasi waktu dalam hari:",min_value=0)
jumlah_tabungan_awal = st.text_input("Masukkan jumlah tabungan yang sudah dimiliki saat ini (isi 0 jika belum memiliki tabungan sama sekali):",0)
jumlah_tabungan_awal=parse_rupiah(jumlah_tabungan_awal)

# Calculate remaining target
sisa_target = target_keuangan - jumlah_tabungan_awal

# Display result
if st.button("HITUNG"):
    if sisa_target > 0:
        tabungan_per_hari = sisa_target / durasi_hari
        st.success(f"Anda perlu menabung sebesar{locale.currency(tabungan_per_hari,grouping=True)} setiap hari.")  

    else:
        st.success("Anda sudah memiliki tabungan yang cukup untuk mencapai target keuangan")
else:
    st.warning("Masukkan nilai yang valid untuk semua input.")