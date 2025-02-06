# Proyek Akhir: Menyelesaikan Permasalahan Institusi Pendidikan (Jaya Jaya Institut)

## Business Understanding
Jaya Jaya Institut menghadapi tantangan besar terkait dengan tingginya tingkat dropout mahasiswa. Proyek ini bertujuan untuk memberikan solusi berbasis data untuk mengidentifikasi faktor-faktor penyebab dropout mahasiswa serta memberikan rekomendasi strategis untuk mengurangi tingkat tersebut. Solusi yang dikembangkan menggunakan pendekatan data science, dimulai dengan pemahaman bisnis hingga implementasi model machine learning yang siap digunakan oleh institusi.

### Permasalahan Bisnis
Tingginya tingkat dropout mahasiswa yang dapat berdampak pada citra dan keberlanjutan operasional institusi. Identifikasi faktor-faktor yang mempengaruhi keputusan mahasiswa untuk berhenti kuliah sangat penting untuk merancang kebijakan pencegahan yang tepat.

### Cakupan Proyek
- **Analisis Faktor Penyebab Dropout**: Menyusun daftar faktor-faktor yang mempengaruhi tingkat dropout mahasiswa berdasarkan data yang tersedia.
- **Pengembangan Model Prediksi Dropout**: Menggunakan algoritma machine learning untuk membangun model prediksi dropout.
- **Deployment Model dan Dashboard Monitoring**: Mengimplementasikan model untuk prediksi dan membuat dashboard untuk memantau data terkait dropout mahasiswa.

### Persiapan
Sumber data: https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv

Setup environment:
```bash
git clone https://github.com/Shacent/Submission-2.git
cd Submission-2
pip install -r requirements.txt
```

## Business Understanding
Business dashboard dibuat menggunakan Metabase, yang memberikan visualisasi data terkait dropout mahasiswa, distribusi pembayaran biaya kuliah, dan analisis faktor penting lainnya. Dashboard ini memungkinkan tim untuk memonitor secara real-time dan menganalisis tren terkait mahasiswa berisiko dropout.
- Link Dashboard: [Metabase Dashboard Link](http://localhost:3000/public/dashboard/5574170d-01c7-4dae-b6a8-703943eb6070)

## Menjalankan Sistem Machine Learning
Prototipe sistem machine learning ini dibuat menggunakan Streamlit untuk mempermudah pengguna dalam mengakses dan menjalankan model prediksi dropout. Model ini menggunakan algoritma Random Forest untuk melakukan prediksi dropout mahasiswa berdasarkan data yang dimasukkan.

- Link Prototipe: [Streamlit Deployment Link](https://jaya-institute-model-deployment.streamlit.app/)

Untuk menjalankan sistem di lingkungan lokal, ikuti langkah-langkah berikut:
1. Clone repository ini:
```bash
git clone https://github.com/Shacent/Submission-2.git
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Jalankan aplikasi Streamlit:
```bash
streamlit run main.py
```
## Conclusion
Berdasarkan analisis data dan model yang dibangun, ditemukan bahwa beberapa faktor utama yang menyebabkan mahasiswa di Jaya Jaya Institut dropout adalah masalah finansial (terutama bagi mahasiswa yang berstatus sebagai debitur), rendahnya nilai akademik (terutama pada semester pertama), dan rendahnya partisipasi mahasiswa dalam kegiatan perkuliahan. Dengan adanya model prediksi ini, pihak institusi dapat melakukan intervensi lebih dini pada mahasiswa yang berisiko tinggi untuk dropout, sehingga tingkat keberhasilan akademik dapat meningkat.

### Rekomendasi Action Items
Berdasarkan analisis data dan temuan model prediksi, berikut adalah rekomendasi lebih lanjut yang dapat diterapkan oleh Jaya Jaya Institut untuk mengurangi tingkat dropout mahasiswa:

1. **Pemantauan Akademik Real-Time:**
    - **Sistem Peringatan Dini (Early Warning System):** Mengembangkan sistem yang secara otomatis memberi peringatan kepada pihak administrasi atau dosen ketika mahasiswa menunjukkan penurunan nilai atau kehadiran yang signifikan. Peringatan ini dapat berbentuk notifikasi otomatis untuk memungkinkan intervensi tepat waktu.
    - **Monitoring Kinerja Akademik Tiap Semester:** Buat sistem dashboard yang menampilkan tren kinerja akademik mahasiswa per semester, termasuk nilai akhir dan partisipasi dalam kegiatan akademik seperti ujian dan tugas. Hal ini memungkinkan dosen atau fakultas untuk melihat perubahan pola belajar yang mungkin mengarah pada risiko dropout.

2. **Bantuan Keuangan dan Program Beasiswa:**
    - **Program Cicilan Pembayaran Biaya Kuliah:** Untuk mahasiswa yang kesulitan membayar biaya kuliah, tawarkan program cicilan yang fleksibel. Sistem ini dapat berbasis data pemantauan finansial mahasiswa yang menunjukkan bahwa mereka kesulitan membayar biaya kuliah pada waktu yang tepat.
    - **Beasiswa Berbasis Kebutuhan:** Implementasikan program beasiswa untuk mahasiswa yang menunjukkan kesulitan finansial namun memiliki kinerja akademik yang baik. Data yang diambil dari sistem dapat digunakan untuk menilai kelayakan mahasiswa yang berhak menerima beasiswa.

3. **Penyediaan Program Akademik dan Kelas Tambahan:**
    - **Program Remedial untuk Mahasiswa dengan Nilai Rendah:** Berdasarkan model prediksi, sediakan kelas remedial untuk mahasiswa yang memiliki nilai rendah terutama pada mata kuliah inti yang berpotensi menghambat kelulusan mereka. Hal ini akan memberikan mereka kesempatan untuk memperbaiki nilai mereka sebelum melanjutkan ke semester berikutnya.
    - **Kelas Peningkatan Akademik (Catch-Up Classes):** Tawarkan kelas tambahan atau kelas malam bagi mahasiswa yang tertinggal di luar jam kuliah reguler. Mahasiswa yang memiliki masalah dalam mengikuti perkuliahan karena alasan waktu atau pekerjaan bisa lebih fleksibel.

4. **Pendampingan dan Konseling Mahasiswa:**
    - **Sesi Konseling Akademik dan Psikologis:** Banyak mahasiswa mengalami masalah psikologis yang dapat mempengaruhi keputusan mereka untuk dropout. Sediakan layanan konseling baik dari sisi akademik maupun psikologis untuk membantu mahasiswa mengatasi stres dan kesulitan yang dihadapi. Data yang dianalisis dapat membantu mengidentifikasi mahasiswa yang berisiko tinggi secara psikologis untuk mendapatkan perhatian lebih.
    - **Kelompok Studi dan Mentoring:** Bentuk kelompok studi atau program mentoring di mana mahasiswa senior atau dosen dapat membantu mahasiswa yang lebih muda dengan masalah akademik atau adaptasi kehidupan kampus.

5. **Penghargaan dan Insentif untuk Meningkatkan Motivasi:**
    - **Insentif Akademik dan Non-Akademik:** Berikan penghargaan berupa beasiswa atau sertifikat bagi mahasiswa yang menunjukkan progres positif atau kemampuan untuk meningkatkan kinerja akademik mereka setelah melakukan intervensi atau mengikuti program remedial.
    - **Pengenalan Mahasiswa Berprestasi:** Tampilkan mahasiswa berprestasi secara reguler melalui media sosial kampus atau papan pengumuman sebagai contoh bagi mahasiswa lain untuk meningkatkan motivasi mereka.

6. **Kampanye Penyuluhan Mengenai Dropout:**
    - **Workshop dan Seminar untuk Mahasiswa Baru:** Adakan sesi penyuluhan di awal semester mengenai pentingnya pemantauan akademik, cara mengatasi stres, dan memanfaatkan layanan kampus yang ada seperti konseling atau bantuan keuangan. Mahasiswa yang lebih memahami apa yang bisa dilakukan ketika mereka menghadapi masalah akan lebih kecil kemungkinannya untuk dropout.
    - **Peningkatan Kesadaran pada Mahasiswa Rentan:** Gunakan data dari model prediksi untuk menargetkan mahasiswa yang memiliki risiko tinggi untuk dropout dan ajak mereka untuk mengikuti sesi penyuluhan atau bantuan khusus.

        

    
    


