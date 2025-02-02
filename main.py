import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

# Judul aplikasi
st.title("🎓 Prediksi Status Mahasiswa (Graduate/Dropout) - Hauzan")

# Memuat model dan scaler
@st.cache_resource  # Cache resource untuk mempercepat loading
def load_model():
    # URL untuk file raw
    model_url = "https://raw.githubusercontent.com/Shacent/Submission-2/main/random_forest_model_fix.pkl"
    scaler_url = "https://raw.githubusercontent.com/Shacent/Submission-2/main/scaler.pkl"
    
    # Path untuk menyimpan file sementara
    model_path = "random_forest_model_fix.pkl"
    scaler_path = "scaler.pkl"
    
    # Unduh model jika belum ada
    if not os.path.exists(model_path):
        with open(model_path, 'wb') as file:
            response = requests.get(model_url)
            file.write(response.content)
    
    # Unduh scaler jika belum ada
    if not os.path.exists(scaler_path):
        with open(scaler_path, 'wb') as file:
            response = requests.get(scaler_url)
            file.write(response.content)
    
    # Muat model dan scaler
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
    
    return model, scaler

rf_model, scaler = load_model()

# Sidebar untuk input fitur
st.sidebar.header("📝 Input Fitur")

# Fungsi untuk mengambil input dari pengguna
def user_input_features():
    col1, col2 = st.sidebar.columns(2)
    
    with col1:
        curricular_1st_sem_grade = st.number_input("Nilai Semester 1", min_value=0.0, max_value=20.0, value=10.0, step=0.1)
        curricular_2nd_sem_grade = st.number_input("Nilai Semester 2", min_value=0.0, max_value=20.0, value=10.0, step=0.1)
        curricular_1st_sem_approved = st.number_input("Mata Kuliah Disetujui Semester 1", min_value=0, max_value=10, value=5)
        curricular_2nd_sem_approved = st.number_input("Mata Kuliah Disetujui Semester 2", min_value=0, max_value=10, value=5)
    
    with col2:
        debtor = st.selectbox("Memiliki Utang?", options=[("Tidak", 0), ("Ya", 1)], format_func=lambda x: x[0])
        tuition_fees_up_to_date = st.selectbox("Membayar Uang Kuliah Tepat Waktu?", options=[("Tidak", 0), ("Ya", 1)], format_func=lambda x: x[0])
        age_at_enrollment = st.number_input("Usia Saat Mendaftar", min_value=17, max_value=50, value=20)
        admission_grade = st.number_input("Nilai Masuk", min_value=0.0, max_value=200.0, value=100.0, step=0.1)

    # Membuat dictionary dari input
    data = {
        'Curricular_units_1st_sem_grade': curricular_1st_sem_grade,
        'Curricular_units_2nd_sem_grade': curricular_2nd_sem_grade,
        'Curricular_units_1st_sem_approved': curricular_1st_sem_approved,
        'Curricular_units_2nd_sem_approved': curricular_2nd_sem_approved,
        'Debtor': debtor[1],
        'Tuition_fees_up_to_date': tuition_fees_up_to_date[1],
        'Age_at_enrollment': age_at_enrollment,
        'Admission_grade': admission_grade
    }

    # Konversi ke DataFrame
    features = pd.DataFrame(data, index=[0])
    return features

# Mengambil input dari pengguna
input_df = user_input_features()

# Normalisasi/Scaling data inputan
input_df_scaled = scaler.transform(input_df)

# Prediksi dengan model
prediction = rf_model.predict(input_df_scaled)
prediction_proba = rf_model.predict_proba(input_df_scaled)

# Menampilkan hasil prediksi
st.subheader("🎯 Hasil Prediksi")
status = "Graduate" if prediction[0] == 1 else "Dropout"
if status == "Graduate":
    st.success(f"🎉 Status Prediksi: **{status}**")
else:
    st.error(f"⚠️ Status Prediksi: **{status}**")

# Menampilkan probabilitas prediksi dengan progress bar
st.subheader("📈 Probabilitas Prediksi")
col1, col2 = st.columns(2)

with col1:
    st.metric(label="Probabilitas Dropout", value=f"{prediction_proba[0][0] * 100:.2f}%")
    st.progress(prediction_proba[0][0])

with col2:
    st.metric(label="Probabilitas Graduate", value=f"{prediction_proba[0][1] * 100:.2f}%")
    st.progress(prediction_proba[0][1])

# Tambahkan CSS untuk styling tambahan
st.markdown(
    """
    <style>
    .stProgress > div > div > div > div {
        background-color: #4CAF50;
    }
    .st-b7 {
        color: white;
    }
    .st-cg {
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)
