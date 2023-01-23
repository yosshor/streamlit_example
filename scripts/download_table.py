import streamlit as st
import xlsxwriter
from io import BytesIO

def download_to_csv(df):
    st.download_button(
    label = "Download data as CSV",
    data = df.to_csv().encode('utf-8'),
    file_name = 'large_df.csv',
    mime = 'text/csv'
    )

def download_to_txt(df):
    st.download_button(
    label = "Download data as txt",
    data = df.to_csv().encode('utf-8'),
    file_name = 'large_df.txt',
    )

def download_to_excel(df):
    output = BytesIO()

    # Write files to in-memory strings using BytesIO
    # See: https://xlsxwriter.readthedocs.io/workbook.html?highlight=BytesIO#constructor
    workbook = xlsxwriter.Workbook(output, {'in_memory': True})
    worksheet = workbook.add_worksheet()
    worksheet.write(df)
    workbook.close()

    st.download_button(
        label="Download Excel workbook",
        data=output.getvalue(),
        file_name="workbook.xlsx",
        mime="application/vnd.ms-excel"
    )