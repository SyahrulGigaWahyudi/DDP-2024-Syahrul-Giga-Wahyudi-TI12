import streamlit as st

st.title('Save Money')
st.image('meme2.png', width=300)

st.caption('Welcome to Save Money! This program will help you find solutions to your financial problems.')

st.title('4Sight')

st.caption('Halo teman-teman, perkenalkan kami dari kelompok 4Sight ingin memberikan kalian sebuah aplikasi sederhana pengatur keuangan sehari-hari kalian!')

st.markdown("<h1 style='color: blue;'>About Us</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='color: limegreen;'>We Are 4Sight</h2>", unsafe_allow_html=True)

st.markdown("<p style='font-size:18px;'>Selamat datang di aplikasi kami, disini kami ingin memperkenalkan diri kami serta menjelaskan setiap aplikasi yang anggota kami buat.</p>", unsafe_allow_html=True)

menu = st.sidebar.selectbox(
    "Pilih Penjelasan:",
    ["About Us", "Kalkulator Cicilan Bulanan", "Perhitungan Diskon Ganda", "Kalkulator Anggaran Bulanan", "Kalkulator Tabungan Target"]
)

if menu == "About Us":
    st.subheader("Anggota Kami")
    st.caption('1. Syahrul Giga Wahyudi')
    st.caption('2. Syifa Zakia Qolbi')
    st.caption('3. Fathiyaturohmah')
    st.caption('4. Muhammad Riandana Pranatha')

elif menu == "Kalkulator Cicilan Bulanan":
    st.markdown("<h2 style='color: red;'>Kalkulator Cicilan Bulanan</h2>", unsafe_allow_html=True)
    st.caption('Pertama ada Kalkulator Cicilan Bulanan yang dibuat oleh anggota kami yaitu Syahrul Giga Wahyudi, nah sekarang kami akan menjelaskan tentang aplikasi ini.')
    
    st.markdown("<p style='font-size:18px; color: yellow;'>Kenapa sih aplikasi ini dibuat?</p>", unsafe_allow_html=True)
    st.caption('Aplikasi ini membantu kamu menghitung cicilan bulanan kalau kamu mau pinjam uang, misalnya untuk beli motor, mobil, rumah, atau kebutuhan lain. Jadi, kamu bisa tahu berapa uang yang harus kamu bayar tiap bulan ke bank atau pemberi pinjaman.')

    st.markdown("<p style='font-size:18px; color: yellow;'>Cara kerjanya gimana?</p>", unsafe_allow_html=True)
    st.caption('1. Masukkan jumlah pinjaman. Kamu tinggal isi berapa uang yang mau kamu pinjam (contohnya: Rp 10.000.000).')
    st.caption('2. Masukkan suku bunga tahunan. Isi bunga yang ditawarkan oleh bank/pemberi pinjaman, misalnya 10% per tahun.')
    st.caption('3. Masukkan lama Pinjaman. Pilih berapa bulan kamu mau nyicil, misalnya 12 bulan (1 tahun).')
    st.caption('4. Klik tombol hitung. Setelah itu, aplikasi bakal ngitung otomatis:')
    st.caption('Cicilan bulanan: Berapa yang harus kamu bayar tiap bulan.')
    st.caption('Total yang harus dibayar: Total semua cicilan yang akan kamu bayar selama periode pinjaman.')
    st.caption('Total bunga: Berapa uang tambahan yang kamu bayar karena bunga.')

    st.markdown("<p style='font-size:18px; color: yellow;'>Kenapa ini berguna?</p>", unsafe_allow_html=True)
    st.caption('Bisa bantu hitung sebelum pinjam uang. Kamu bisa lihat dulu apakah cicilan itu cocok sama gaji atau penghasilan kamu, jadi nggak kaget di tengah jalan.')
    st.caption('Coba simulasi. Misalnya, kamu bingung mau pilih bunga 5% selama 2 tahun atau 10% selama 1 tahun. Kamu bisa coba hitung semua opsi buat pilih yang paling ringan.')
    st.caption('Hemat waktu. Nggak perlu ribet ngitung pakai kalkulator biasa atau minta bantuan orang lain. Kamu bisa langsung tahu hasilnya dalam hitungan detik.')

    st.markdown("<p style='font-size:18px; color: yellow;'>Contohnya?</p>", unsafe_allow_html=True)
    st.caption('Bayangkan kamu pinjam Rp 12.000.000 dengan bunga 6% per tahun selama 24 bulan. Aplikasi ini akan kasih tahu:')
    st.caption('Cicilan bulanan kamu: Rp 552.083')
    st.caption('Total yang harus dibayar: Rp 13.250.000')
    st.caption('Total bunga: Rp 1.250.000')
    st.caption('Jadi, kamu tahu kalau selain bayar utang pokok (Rp 12 juta), ada tambahan Rp 1,25 juta karena bunga.')

elif menu == "Perhitungan Diskon Ganda":
    st.markdown("<h2 style='color: red;'>Perhitungan Diskon Ganda</h2>", unsafe_allow_html=True)
    st.caption('Nah, selanjutnya ada Perhitungan Diskon Ganda yang dibuat oleh anggota kami yaitu Syifa Zakia Qolbi')

    st.markdown("<p style='font-size:18px; color: yellow;'>Apa kegunaan Aplikasi ini?</p>", unsafe_allow_html=True)
    st.caption('Aplikasi ini dibuat untuk menghitung diskon ganda pada sebuah barang. Kalau kamu sering belanja dan nemu barang dengan promo "Diskon 20% + 10%", aplikasi ini bisa membantu menghitung harga akhir barang setelah kedua diskon diterapkan. Selain itu, kamu juga bisa lihat berapa uang yang berhasil dihemat.')

    st.markdown("<p style='font-size:18px; color: yellow;'>Fungsi Utamanya</p>", unsafe_allow_html=True)
    st.caption('1. Menghitung Diskon Pertama. Kamu bisa tahu harga barang setelah diskon pertama dan berapa penghematan dari diskon ini.')
    st.caption('2. Menghitung Diskon Kedua. Kalau barang sudah kena diskon pertama, aplikasi juga bisa menghitung diskon kedua berdasarkan harga yang sudah didiskon sebelumnya.')
    st.caption('3. Menggabungkan Kedua Diskon. Menampilkan harga akhir setelah kedua diskon diterapkan secara berurutan, dan menunjukkan total penghematan yang kamu dapatkan.')

    st.markdown("<p style='font-size:18px; color: yellow;'>Cara kerjanya?</p>", unsafe_allow_html=True)
    st.caption('1. Masukkan Harga Awal. Kamu isi harga awal barang, misalnya Rp 1.000.000.')
    st.caption('2. Masukkan Diskon Pertama dan Kedua. Isi persentase diskon pertama dan kedua (contoh: 20% dan 10%).')
    st.caption('3. Pilih Hasil yang Ingin Ditampilkan. Ada tiga pilihan:')
    st.caption('A. Diskon Pertama: Hasil dari diskon pertama saja.')
    st.caption('B. Diskon Kedua: Hasil dari diskon kedua setelah diskon pertama diterapkan.')
    st.caption('C. Diskon Gabungan: Hasil akhir setelah kedua diskon digabung.')

    st.markdown("<p style='font-size:18px; color: yellow;'>Contoh penggunaan</p>", unsafe_allow_html=True)
    st.caption('Misalnya, harga barang Rp 1.000.000, dengan diskon pertama 20% dan diskon kedua 10%. Aplikasi ini akan membantu menghitung:')
    st.caption('1. Harga setelah diskon pertama: Rp 800.000')
    st.caption('2. Harga setelah diskon kedua: Rp 720.000')
    st.caption('3. Total penghematan: Rp 280.000')
    st.caption('Kamu jadi nggak perlu bingung hitung manual, terutama kalau diskon kedua dihitung dari harga yang sudah didiskon pertama.')

    st.markdown("<p style='font-size:18px; color: yellow;'>Aplikasi ini cocok banget untuk:</p>", unsafe_allow_html=True)
    st.caption('1. Pembeli online/offline yang ingin tahu harga akhir dari diskon berlapis.')
    st.caption('2. Penjual yang ingin menjelaskan potongan harga ke pelanggan dengan lebih jelas.')
    st.caption('3. Siapa saja yang ingin memastikan diskon dihitung dengan benar.')

elif menu == "Kalkulator Anggaran Bulanan":
    st.markdown("<h2 style='color: red;'>Kalkulator Anggaran Bulanan</h2>", unsafe_allow_html=True)
    st.caption('Nah, selanjutnya ada aplikasi yang dibuat oleh anggota kami yaitu Tia atau Fathiyaturohmah, ini dia penjelasannya.')

    st.markdown("<p style='font-size:18px; color: yellow;'>Apa kegunaan aplikasi ini?</p>", unsafe_allow_html=True)
    st.caption('Aplikasi ini adalah kalkulator anggaran bulanan yang membantu kamu mengelola keuangan. Dengan aplikasi ini, kamu bisa mencatat gaji bulanan, memasukkan pengeluaran di berbagai kategori, dan melihat apakah keuangan kamu sehat atau tidak.')

    st.markdown("<p style='font-size:18px; color: yellow;'>Fungsi utamanya</p>", unsafe_allow_html=True)
    st.caption('1. Mencatat Gaji Bulanan. Kamu bisa masukkan jumlah gaji yang kamu terima setiap bulan.')
    st.caption('2. Mencatat Pengeluaran Per Kategori. Ada kategori-kategori seperti makanan, transportasi, perumahan, kesehatan, hiburan, tabungan, dan lainnya. Kamu isi berapa uang yang kamu habiskan untuk setiap kategori.')
    st.caption('3. Menghitung Sisa Gaji. Setelah total pengeluaran dihitung, aplikasi akan menunjukkan sisa gaji kamu. Kalau pengeluaran lebih besar dari gaji, akan ada peringatan.')

    st.markdown("<p style='font-size:18px; color: yellow;'>Bagaimana cara kerjanya?</p>", unsafe_allow_html=True)
    st.caption('A. Masukkan jumlah gaji bulanan. Contoh: Rp 5.000.000.')
    st.caption('B. Isi pengeluaran untuk tiap kategori. Misalnya:')
    st.caption('- Makanan: Rp 1.000.000')
    st.caption('- Transportasi: Rp 500.000')
    st.caption('- Perumahan: Rp 2.000.000')
    st.caption('- Tabungan: Rp 500.000. Total pengeluaran jadi Rp 4.000.000.')
    st.caption('C. Aplikasi otomatis menghitung sisa gaji. Dari contoh di atas, sisa gaji kamu adalah Rp 1.000.000.')
    st.caption('D. Hasilnya ditampilkan di layar, termasuk:')
    st.caption('- Total pengeluaran.')
    st.caption('- Sisa gaji.')
    st.caption('- Peringatan kalau pengeluaran lebih besar dari gaji.')

    st.markdown("<p style='font-size:18px; color: yellow;'>Kenapa aplikasi ini berguna?</p>", unsafe_allow_html=True)
    st.caption('* Mengatur keuangan lebih mudah. Kamu bisa tahu ke mana uang kamu habis setiap bulan, jadi nggak bingung kenapa uang cepat habis.')
    st.caption('* Memastikan keuangan sehat. Dengan melihat sisa gaji, kamu bisa menilai apakah pengeluaran kamu sudah sesuai atau perlu dikurangi.')
    st.caption('* Mendorong menabung. Karena ada kategori tabungan, aplikasi ini juga memotivasi kamu untuk menyisihkan uang setiap bulan.')

    st.markdown("<p style='font-size:18px; color: yellow;'>Contoh penggunaan</p>", unsafe_allow_html=True)
    st.caption('Misalnya gaji kamu Rp 6.000.000 dan pengeluaran di berbagai kategori mencapai Rp 6.500.000. Aplikasi ini akan memberi peringatan "Pengeluaran Anda melebihi gaji bulanan!" supaya kamu sadar dan segera mengevaluasi pengeluaran.')
    st.caption('Aplikasi ini cocok untuk siapa saja yang ingin lebih rapi mengelola keuangan pribadi atau keluarga.')

elif menu == "Kalkulator Tabungan Target":
    st.markdown("<h2 style='color: red;'>Kalkulator Tabungan Target</h2>", unsafe_allow_html=True)
    st.caption('Nah, terakhir ini ada aplikasi dari anggota kami yaitu Saki atau Muhammad Riandana Pranatha. Simak yuk penjelasan tentang aplikasinya.')

    st.markdown("<p style='font-size:18px; color: yellow;'>Apasih kegunaan aplikasi ini?</p>", unsafe_allow_html=True)
    st.caption('Aplikasi ini adalah kalkulator tabungan target yang membantu kamu menentukan jumlah uang yang perlu ditabung setiap hari untuk mencapai target keuangan dalam waktu tertentu. Dengan aplikasi ini, kamu bisa membuat rencana menabung yang lebih terarah dan realistis.')

    st.markdown("<p style='font-size:18px; color: yellow;'>Apa fungsi utamanya?</p>", unsafe_allow_html=True)
    st.caption('1. Menghitung Tabungan Harian. Aplikasi menghitung jumlah uang yang harus kamu tabung setiap hari berdasarkan:')
    st.caption('- Target keuangan yang ingin dicapai.')
    st.caption('- Durasi waktu (dalam hari).')
    st.caption('- Jumlah tabungan awal yang sudah kamu miliki.')
    st.caption('2. Mengevaluasi Kecukupan Tabungan. Kalau tabungan awal kamu sudah cukup atau lebih dari target, aplikasi akan memberi tahu bahwa kamu tidak perlu menabung lagi.')

    st.markdown("<p style='font-size:18px; color: yellow;'>Cara kerjanya gimana tuh?</p>", unsafe_allow_html=True)
    st.caption('1. Masukkan Target Keuangan. Kamu isi nominal yang ingin dicapai, misalnya Rp 10.000.000.')
    st.caption('2. Masukkan Durasi Waktu. Tentukan berapa hari yang tersedia untuk mencapai target, misalnya 100 hari.')
    st.caption('3. Masukkan Tabungan Awal. Kalau kamu sudah punya tabungan, isi nominalnya (contoh: Rp 2.000.000). Kalau belum, isi 0.')
    st.caption('4. Tekan Tombol "HITUNG". Aplikasi akan:')
    st.caption('- Menghitung sisa target keuangan (target - tabungan awal).')
    st.caption('- Membagi sisa target dengan jumlah hari untuk mendapatkan jumlah tabungan harian.')

    st.markdown("<p style='font-size:18px; color: yellow;'>Contoh pengggunaanya?</p>", unsafe_allow_html=True)
    st.caption('Misalnya:')
    st.caption('- Target keuangan: Rp 10.000.000')
    st.caption('- Durasi: 100 hari')
    st.caption('- Tabungan awal: Rp 2.000.000')
    st.caption('Sisa target: Rp 8.000.000')
    st.caption('Tabungan per hari: Rp 8.000.000 ÷ 100 = Rp 80.000')
    st.caption('Aplikasi akan menampilkan: "Anda perlu menabung sebesar Rp 80.000 setiap hari."')

    st.markdown("<p style='font-size:18px; color: yellow;'>Kenapa sih aplikasi ini berguna?</p>", unsafe_allow_html=True)
    st.caption('1. Membantu Perencanaan Keuangan. Kamu bisa tahu langkah konkret untuk mencapai target, seperti membeli barang impian, liburan, atau dana darurat.')
    st.caption('2. Memotivasi untuk Menabung. Dengan angka yang jelas, menabung terasa lebih ringan karena target harian lebih kecil dibandingkan melihat total besar sekaligus.')
    st.caption('3. Menyadarkan Kemampuan Finansial. Kalau sisa target terasa terlalu berat dalam waktu singkat, kamu bisa mempertimbangkan ulang durasi atau target.')
    st.caption('Aplikasi ini cocok untuk siapa saja yang ingin merencanakan keuangan dengan lebih baik dan terorganisir')