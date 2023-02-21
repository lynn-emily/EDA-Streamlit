import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
import streamlit.components.v1 as components

# Functions
def generate_profile_report(df):
    return ProfileReport(df, explorative=True)

def display_profile_report(profile_report):
    with st.spinner("Generating profile report..."):
        components.html(profile_report.to_html(), height=1000, scrolling=True)
        
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
    
st.title("Generate a Profile Report on your data")
    
    
#if st.session_state.file is not None:
if st.session_state.df is not None:
    #st.session_state.file.seek(0) # https://stackoverflow.com/questions/64347681/emptydataerror-no-columns-to-parse-from-file-about-streamlit
    #df = pd.read_csv(st.session_state.uploaded_file)
    cols = st.session_state.df.columns.to_list()
    col_selections = []
    select_all = False

    with st.expander('Choose what columns to include in the profile report'):
        with st.form('my_form'):
            select_all = st.checkbox('All columns')
            for i, col in enumerate(cols):
                col_selections.append(st.checkbox(col))

            submitted = st.form_submit_button('Submit and Generate Profile Report')
        
    if submitted:
        col_df = None
        if select_all:
            col_df = st.session_state.df
        else:
            col_selections_series = pd.Series(col_selections)
            col_df = st.session_state.df[st.session_state.df.columns[col_selections_series]]
        profile_report = generate_profile_report(col_df)
        display_profile_report(profile_report)       
else:
    st.write('Please upload a data file to see results here')