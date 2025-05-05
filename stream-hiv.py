import pickle
import streamlit as st

# Membaca model
hiv_model = pickle.load(open(HIV_model.sav))

# Judul Web
st.title('Data Mining Clustering HIV')