import pickle
import streamlit as st

# Membaca model
hiv_model = pickle.load(open('HIV_model.sav', 'rb'))

# Judul Web
st.title('Data Mining Clustering HIV')

# Membagi kolom
col1, col2 = st.columns(2)

# Indentifikasi inputan 
with col1 :
    Umur = st.text_input('Input Nilai Umur')

with col2 :
    Jenis_Kelamin = st.text_input('Input Nilai Jenis Kelamin')

with col1 :
    Kecamatan = st.text_input('Input Nilai Jenis Kecamatan')

with col2 :
    Kelurahan = st.text_input('Input Nilai Jenis Kelurahan')

with col1 :
    Tahun_Register = st.text_input('Input Nilai Jenis Tahun Register')

# Code untuk clustering
hiv_diagnosis = ''

# Membuat tombol untuk clustering
if st.button('Test Clustering HIV'):
    hiv_clustering = hiv_model.cluster([[Umur, Jenis_Kelamin, Kecamatan, 
                                         Kelurahan, Tahun_Register]])

    if hiv_clustering[0] == 0:
        hiv_diagnosis = 'Status ODHIV Gagal Follow Up'
    elif hiv_clustering[0] == 1:
        hiv_diagnosis = 'Status ODHIV Meninggal'
    else:
        hiv_diagnosis = 'Status ODHIV Sedang Pengobatan'

    st.success(hiv_diagnosis)
