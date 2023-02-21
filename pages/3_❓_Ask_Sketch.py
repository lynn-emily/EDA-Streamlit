import streamlit as st
import pandas as pd
import asyncio
# https://github.com/streamlit/streamlit/issues/744
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

import sketch
import streamlit.components.v1 as components
from IPython.display import HTML, display
import uuid
import base64
import json

def to_b64(data):
    return base64.b64encode(json.dumps(data).encode("utf-8")).decode("utf-8")

def run_code(code):
    try:
        st.write("Hello!")
    except:
        st.write("Sorry, could not run the above code")


# Page
st.set_page_config(
    layout='wide',
    page_title='Data Profiling and Quality App',
    page_icon="📈"
)

st.title("Ask Sketch to help you explore your data!")

if st.session_state.file is not None:
    st.session_state.file.seek(0)

    df = pd.read_csv(st.session_state.file)

    st.header("Your Data:")
    st.dataframe(df)

    with st.form("my_form"):
        request_type = st.radio(
            label="What type of request is this?",
            options=['Asking a question about my data', 'Asking how to write some code'],
            index=0
        )

        request = st.text_area(
            label="What is your request?",
            value="",
            height=50,
            max_chars=500
        )

        submitted = st.form_submit_button("Submit")

    if submitted:
        if request != "":
            answer = df.sketch.ask(request, call_display=False)
            st.code(answer)

#             st.session_state.run_code = False
#             click = st.button('Run code on data')
            
#             if click:
#                 st.session_state.run_code = True
                
#             if st.session_state.run_code == True:
#                 try:
#                     st.write("Hello!")
#                 except:
#                     st.write("Sorry, could not run the above code")

else:
    st.write('Please upload a data file in order to ask a question.')