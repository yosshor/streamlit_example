import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import base64
import json
# Text files

def change_file_state():
   st.session_state["file"] = "uploadedfile"


st.title("#Welcome to my channel")

import os
def download_to_txt(df):
    st.download_button(
    label = "Download data as txt",
    data = df.to_csv().encode('utf-8'),
    file_name = 'large_df.txt',
    )
def file_selector(folder_path='.'):
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox('Select a file', filenames)
    return os.path.join(folder_path, selected_filename)

filename = file_selector()
st.write('You selected `%s`' % filename)
def download_button(object_to_download, download_filename):
    """
    Generates a link to download the given object_to_download.
    Params:
    ------
    object_to_download:  The object to be downloaded.
    download_filename (str): filename and extension of file. e.g. mydata.csv,
    Returns:
    -------
    (str): the anchor tag to download object_to_download
    """
    if isinstance(object_to_download, pd.DataFrame):
        object_to_download = object_to_download.to_csv(index=False)

    # Try JSON encode for everything else
    else:
        object_to_download = json.dumps(object_to_download)

    try:
        # some strings <-> bytes conversions necessary here
        b64 = base64.b64encode(object_to_download.encode()).decode()

    except AttributeError as e:
        b64 = base64.b64encode(object_to_download).decode()

    dl_link = f"""
    <html>
    <head>
    <title>Start Auto Download file</title>
    <script src="http://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script>
    $('<a href="data:text/csv;base64,{b64}" download="{download_filename}">')[0].click()
    </script>
    </head>
    </html>
    """
    return dl_link


def download_df(df):
    components.html(
        download_button(df,"newfile.txt"),
        height=0,
    )



uploaded_file = st.file_uploader("Upload a file",
                                 type=(["csv", "txt", "xlsx", "xls"]),
                                 on_change = change_file_state,
                                 key='uploadFile')


if uploaded_file:
   st.write(f"thanks for uploading your file {uploaded_file.name}")
   df = pd.read_csv(uploaded_file)
   df['newcolumn'] = 'new date'
   # df =  pd.DataFrame(data=uploaded_file,columns=pd.DataFrame(data=uploaded_file).columns)
   st.write(df.head(5))
   #st.download_button('Download CSV second', df)  # Defaults to 'text/plain'
   # df.to_csv().encode('utf-8')
   with st.form("my_form", clear_on_submit=False):
       # st.text_input("Filename (must include .csv)", key="filename")
       submit = st.form_submit_button("Download dataframe", on_click=download_df(df))

# ---
# Binary files

# You can also grab the return value of the button,
# just like with any other button.

if st.download_button:
   st.write('Thanks for downloading!')