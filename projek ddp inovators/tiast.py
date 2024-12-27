import streamlit as st

# Title and description
st.title("\U0001F4B8 Kalkulator Anggaran Bulanan")
st.write("Kelola pengeluaran Anda dengan mudah dan ketahui sisa gaji Anda.")

# Fungsi untuk mengonversi input dengan format ribuan (titik) ke angka
def convert_to_number(value):
    if value:
        value = value.replace('.', '')  # Menghapus titik
        # Mengecek apakah input hanya berisi angka
        if value.isdigit():
            return float(value)
        else:
            return None  # Mengembalikan None jika ada huruf atau karakter lain
    return 0.0

# Input: Gaji bulanan dengan format ribuan
gaji_bulanan = st.text_input("Masukkan gaji bulanan Anda (Rp):", "0")
gaji_bulanan = convert_to_number(gaji_bulanan)

# Kategori pengeluaran
kategori = [
    "Makanan",
    "Transportasi",
    "Perumahan",
    "Pendidikan",
    "Kesehatan",
    "Hiburan",
    "Tabungan"
]

st.subheader("Masukkan pengeluaran untuk setiap kategori:")
pengeluaran_dict = {}
total_pengeluaran = 0

# Menggunakan text_input agar format ribuan bisa diproses
for k in kategori:
    pengeluaran = st.text_input(f"{k} (Rp):", "0")
    pengeluaran = convert_to_number(pengeluaran)
    if pengeluaran is None:
        st.error(f"Pengeluaran untuk {k} harus berupa angka dengan format yang valid.")
        pengeluaran = 0  # Reset nilai jika input tidak valid
    pengeluaran_dict[k] = pengeluaran
    total_pengeluaran += pengeluaran

# Validasi untuk memastikan input gaji dan pengeluaran tidak kosong atau tidak valid
if st.button("Hitung Sisa Gaji"):
    if gaji_bulanan == 0 or total_pengeluaran == 0:
        st.error("Harap masukkan gaji dan pengeluaran yang valid untuk menghitung sisa gaji.")
    elif gaji_bulanan is None:
        st.error("Gaji bulanan harus berupa angka dengan format yang valid.")
    elif total_pengeluaran > gaji_bulanan:
        st.error("Pengeluaran Anda melebihi gaji bulanan!")
    else:
        # Hitung sisa gaji jika semua input valid
        st.subheader("Rincian Anggaran Bulanan")
        st.write(f"**Gaji Bulanan:** Rp {gaji_bulanan:,.2f}")
        st.write(f"**Total Pengeluaran:** Rp {total_pengeluaran:,.2f}")
        st.write(f"**Sisa Gaji:** Rp {gaji_bulanan - total_pengeluaran:,.2f}")

        st.success("Keuangan Anda terkendali.")
else:
    st.warning("input semua nilai yang benar")