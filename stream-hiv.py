import pickle
import streamlit as st

# Membaca model
hiv_model = pickle.load(open('HIV_model.sav', 'rb'))

# Judul Web
st.title('Data Mining Clustering HIV')

# Indentifikasi inputan 
Umur = st.text_input('Input Nilai Umur')

Jenis_Kelamin = st.text_input('Input Nilai Jenis Kelamin')

Kecamatan = st.text_input('Input Nilai Jenis Kecamatan')

Kelurahan = st.text_input('Input Nilai Jenis Kelurahan')

Tahun_Register = st.text_input('Input Nilai Jenis Tahun Register')

# Code untuk clustering
hiv_diagnosis = ''

# Membuat tombol untuk clustering
if st.button('Test Clustering HIV'):
    hiv_clustering = hiv_model.kmeans([[Umur, Jenis_Kelamin, Kecamatan, 
                                         Kelurahan, Tahun_Register]])

    if hiv_clustering[0] == 0:
        hiv_diagnosis = 'Status ODHIV Gagal Follow Up'
    elif hiv_clustering[0] == 1:
        hiv_diagnosis = 'Status ODHIV Meninggal'
    else:
        hiv_diagnosis = 'Status ODHIV Sedang Pengobatan'

    st.success(hiv_diagnosis)
