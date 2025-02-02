# Analisis Prediksi Dropout Mahasiswa - Jaya Jaya Institut

## Deskripsi Proyek
Jaya Jaya Institut menghadapi permasalahan tingkat dropout mahasiswa yang tinggi. Proyek ini bertujuan untuk mengidentifikasi faktor-faktor penyebab dropout mahasiswa dan memberikan solusi berbasis data yang dapat membantu institusi melakukan intervensi dini. Proyek ini dilakukan menggunakan pendekatan data science yang mencakup proses end-to-end, dari business understanding hingga deployment.

---

## Struktur Proyek
Proyek ini menggunakan struktur templat proyek yang telah disediakan. Berikut adalah rincian strukturnya:

- **Business Understanding**: Penjelasan masalah, tujuan, dan parameter kesuksesan.
- **Data Understanding**: Eksplorasi dataset, analisis fitur penting, dan visualisasi data awal.
- **Data Preparation**: Pembersihan data dan transformasi fitur untuk digunakan dalam model machine learning.
- **Modeling**: Pengembangan model prediksi menggunakan algoritma Random Forest.
- **Evaluation**: Evaluasi model berdasarkan metrik kinerja seperti akurasi, presisi, recall, dan F1-score.
- **Deployment**: Implementasi model machine learning dan dashboard monitoring menggunakan Streamlit dan Metabase.

---

## Tools yang Digunakan
- **Python**: Untuk analisis data, pemrosesan, dan pengembangan model machine learning.
- **Streamlit**: Untuk membuat prototipe solusi machine learning yang siap digunakan.
- **Metabase**: Untuk pembuatan dashboard monitoring data.
- **Docker**: Untuk menyimpan dan mengekspor instance database Metabase.

---

## Tahapan Proyek

### 1. Business Understanding
**Masalah**: Tingginya tingkat dropout mahasiswa di Jaya Jaya Institut.

**Tujuan**:
- Mengidentifikasi faktor-faktor utama yang menyebabkan mahasiswa dropout.
- Memberikan rekomendasi actionable untuk mengurangi tingkat dropout.

---

### 2. Data Understanding
**Dataset**:
Dataset mencakup informasi seperti mata kuliah yang diselesaikan, nilai penerimaan, pembayaran biaya kuliah, usia pendaftaran, dan lainnya.

**Fitur Penting**:
1. `Curricular_units_2nd_sem_approved`
2. `Tuition_fees_up_to_date`
3. `Curricular_units_1st_sem_approved`
4. `Curricular_units_2nd_sem_grade`
5. `Admission_grade`
6. `Debtor`
7. `Age_at_enrollment`

---

### 3. Data Preparation
- Membersihkan data dengan menangani nilai kosong dan outlier.
- Menggunakan teknik standardisasi pada fitur numerik untuk mempersiapkan data ke model.

---

### 4. Modeling
- Algoritma yang digunakan: **Random Forest**
- Hasil evaluasi model:
  - Akurasi: 93%
  - F1-score: {0:95%} , {1:90}
  - recall: {0:94%} , {1:92}
---

### 5. Deployment

#### a. Solusi Machine Learning
**Prototipe Streamlit**: 
- URL Prototipe: [Streamlit Deployment Link]([https://streamlit.app/](https://jaya-institute-model-deployment.streamlit.app/))
- Fitur:
  - Input data mahasiswa.
  - Prediksi apakah mahasiswa akan dropout atau tidak.
  - Visualisasi probabilitas dropout.

#### b. Dashboard Monitoring
**Metabase/Tableau/Looker Studio**:
- **Dashboard Link**: [Dashboard Monitoring]([https://metabase-link.com/](https://github.com/Shacent/Submission-2/blob/main/Jaya%20Jaya%20Institute%20Dashboard%20-%20Hauzan.pdf))
- Fitur:
  - Visualisasi distribusi dropout mahasiswa.
  - Analisis fitur penting (feature importance).
  - Tren pembayaran biaya kuliah.

---

## Action Items
Berdasarkan hasil analisis, berikut adalah rekomendasi untuk Jaya Jaya Institut:

### 1. Pemantauan Akademik
- Implementasikan sistem monitoring nilai dan kehadiran secara real-time.
- Terapkan early warning system untuk mengidentifikasi mahasiswa berisiko tinggi.

### 2. Bantuan Keuangan
- Sediakan program cicilan pembayaran biaya kuliah.
- Alokasikan anggaran untuk beasiswa berbasis kebutuhan finansial.

### 3. Dukungan Khusus untuk Kelompok Rentan
- Sediakan kelas malam dan program fleksibel untuk mahasiswa dewasa.
- Implementasikan program remedial untuk mahasiswa dengan nilai penerimaan rendah.

### 4. Penghargaan untuk Meningkatkan Motivasi
- Berikan penghargaan akademik dan non-akademik kepada mahasiswa yang menunjukkan progres positif.

### 5. Evaluasi dan Monitoring Berkala
- Lakukan survei tahunan dan laporan bulanan untuk memantau progres mahasiswa.

---

## Cara Menjalankan Prototipe
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


## Informasi Tambahan
### Email dan Password Metabase:
- Email: `hauzandini@mail.com`
- Password: `Shacent.54321`

