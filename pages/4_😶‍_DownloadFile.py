import streamlit as st
import pandas as pd
from scripts import download_table
# Text files

def change_file_state():
   st.session_state["file"] = "uploadedfile"


st.title("#Welcome to my channel")

import os

def file_selector(folder_path='.'):
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox('Select a file', filenames)
    return os.path.join(folder_path, selected_filename)

filename = file_selector()
st.write('You selected `%s`' % filename)


uploaded_file = st.file_uploader("Upload a file",
                                 type=(["csv", "txt", "xlsx", "xls"]),
                                 on_change = change_file_state,
                                 key='uploadFile')
global df



if uploaded_file:
    if uploaded_file.name.split('.')[1] == 'csv' :
       st.write(f"thanks for uploading your file {uploaded_file.name}")
       df = pd.read_csv(uploaded_file)
       df['newcolumn'] = 'new date'
       # df =  pd.DataFrame(data=uploaded_file,columns=pd.DataFrame(data=uploaded_file).columns)
       st.write(df.head(5))
      # st.download_button('Download CSV', df)  # Defaults to 'text/plain'
       download_table.download_to_csv(df)

    elif uploaded_file.name.split('.')[1] == 'xlsx' or uploaded_file.name.split('.')[1] == 'xls' :
        st.write(f"thanks for uploading your file {uploaded_file}")
        df = pd.read_excel(uploaded_file)
        df['newcolumn'] = 'new date'
        # df =  pd.DataFrame(data=uploaded_file,columns=pd.DataFrame(data=uploaded_file).columns)
        st.write(df.head(5))
        download_table.download_to_csv(df)

    if uploaded_file.name.split('.')[1] == 'txt':
       st.write(f"thanks for uploading your file {uploaded_file.name}")
       df = pd.read_csv(uploaded_file)
       df['newcolumn'] = 'new date'
       # df =  pd.DataFrame(data=uploaded_file,columns=pd.DataFrame(data=uploaded_file).columns)
       st.write(df.head(5))
       #st.download_button('Download CSV second', df)  # Defaults to 'text/plain'
       download_table.download_to_txt(df)

# ---
# Binary files

# You can also grab the return value of the button,
# just like with any other button.

if st.download_button:
   st.write('Thanks for downloading!')