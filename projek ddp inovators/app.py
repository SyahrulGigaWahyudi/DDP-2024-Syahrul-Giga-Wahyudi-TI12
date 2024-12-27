import streamlit as st

# Definisi halaman dan navigasi
pages = {
    "HOME": [
        st.Page("home.py", title="Home"),
    ],
    "APLIKASI": [
        st.Page("gigast.py", title="Kalkulator Cicilan Bulanan"),
        st.Page("sakist.py", title="Kalkulator Tabungan Target"),
        st.Page("sifast.py", title="Kalkulator Diskon Ganda"),
        st.Page("tiast.py", title="Kalkulator Anggaran Bulanan"),
    ]
}

# Sidebar navigasi
pg = st.navigation(pages)

# Jalankan halaman yang dipilih
pg.run()