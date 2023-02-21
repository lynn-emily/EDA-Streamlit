import streamlit as st
import random
import pandas as pd


def upload_data_file():
    st.session_state.file = None
    st.session_state.df = None
    file = st.file_uploader(
        label='Upload Data File',
        type=["csv","xlsx","xls"]
    )
    if file is not None:
        load_data(file)
       
    
def load_data(file):
    st.session_state.file = file
    df = pd.read_csv(file)
    st.session_state.df = df
    
    
    
# Page
st.set_page_config(
    layout='wide',
    page_title='Data Profiling and Quality App',
    page_icon="📈"
)

# Configure session state
if 'file' not in st.session_state:
    st.session_state.file = None
if 'df' not in st.session_state:
    st.session_state.df = None

    
if st.session_state.file is None:
    upload_data_file()
    