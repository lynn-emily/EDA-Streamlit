import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
import sweetviz as sv
import codecs


def st_display_sweetviz(report_html):
    report_file = codecs.open(report_html, 'r')
    page = report_file.read()
    components.html(page, height=1000, scrolling=True)


# Configure session state
if 'file' not in st.session_state:
    st.session_state.file = None
if 'df' not in st.session_state:
    st.session_state.df = None

# Page
st.set_page_config(
    layout='wide',
    page_title='Data Profiling and Quality App',
    page_icon="📈"
)
    
st.title("Explore your data with SweetViz")

if st.session_state.df is not None:
    cols = st.session_state.df.columns.to_list()
    col_selections = []
    select_all = False
    target = 'No target'
    
    with st.expander('Choose what columns to explore:'):
        with st.form('my_form'):
            select_all = st.checkbox('All columns')
            for i, col in enumerate(cols):
                col_selections.append(st.checkbox(col))
                
            radio_options = ['No target'] + cols
            target = st.radio('Target variable:', options=radio_options, index=0)

            submitted = st.form_submit_button('Submit and Generate Sweetviz Report')
            
        
    if submitted:
        col_df = None
        if select_all:
            col_df = st.session_state.df
        else:
            col_selections_series = pd.Series(col_selections)
            col_df = st.session_state.df[st.session_state.df.columns[col_selections_series]]
        
        if target == 'No target':
            report = sv.analyze(col_df)
        else:
            report = sv.analyze(source=col_df, target_feat=target)
        #report.show_html(layout='vertical')
        report.show_html(layout='vertical', open_browser=False)
        components.iframe(src='http://localhost:3001/SWEETVIZ_REPORT.html', width=1100, height=1200, scrolling=True)
        #st_display_sweetviz("SWEETVIZ_REPORT.html")
        #st.components.v1.html(report.show_notebook(layout='vertical'), height=1000, scrolling=True)
        