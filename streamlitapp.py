import streamlit as st
import pandas as pd
#with open('styles.css') as f:
    #st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)
def process_files(uploaded_file):
    if uploaded_file:
        df = pd.read_excel(uploaded_file, nrows=30)
        
        if st.button("Download Duplicate flagged"):
            # Check for duplicates in the first column by default and remove them
            deduplicated = flag_duplicates(df)
            st.download_button("Download Duplicated flagged", deduplicated.to_csv(), key='download_duplicates', mime='text/csv')

        if st.button("Go To Material Classification"):
            show_material_classification(df)

def flag_duplicates(df):
    # Your duplicate flagging logic here
    pass

def show_material_classification(df):
    st.title("Material Classification")
    uploaded_file = st.file_uploader("Upload file for material classification", type=["xlsx", "xls", "csv"])
    # Your Material Classification page content here
    # You can create widgets and display relevant information on this page

def main():
    st.title("Microsoft Project")

    uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx", "xls", "csv"])

    if uploaded_file is not None:
        file_extension = uploaded_file.name.split('.')[-1]

        if file_extension in ('xlsx', 'xls'):
            st.text("Excel file uploaded.")
            process_files(uploaded_file)
        elif uploaded_file.name.endswith('.csv'):
            process_files(uploaded_file)
        else:
            st.text("Unsupported file type. Please upload an Excel file (XLSX or XLS).")



if __name__ == "__main__":
    main()
