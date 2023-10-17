import streamlit as st
import pandas as pd
import time

def process_files(uploaded_file):
    if uploaded_file:
        df = pd.read_excel(uploaded_file, nrows=30)

        if st.button("Download Duplicate flagged"):
            deduplicated = flag_duplicates(df)
            st.download_button("Download Duplicated flagged", deduplicated.to_csv(), key='download_duplicates', mime='text/csv')

        if st.button("Go To Material Classification"):
            st.experimental_set_query_params(material_classification=True)  # Switch to Material Classification page

def flag_duplicates(df):
    # Your duplicate flagging logic here
    pass

def process(uploaded_file):
    try:
        if uploaded_file:
            st.text("Your file is being processed...")
            # Replace this with your actual classification logic
            time.sleep(5)
            st.text("Processing complete. Here are the results: ")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

def material_classification_page():
    st.title("Material Classification")
    uploaded = st.file_uploader("Upload file for material classification", type=["xlsx", "xls", "csv"])
    if uploaded is not None:
        file_extension = uploaded.name.split('.')[-1].lower()

        if file_extension in ('xlsx', 'xls'):
            st.text("Excel file uploaded.")
            process(uploaded)
        elif file_extension == 'csv':
            st.text("CSV file uploaded.")
            process(uploaded)
        else:
            st.text("Unsupported file type. Please upload an Excel file (XLSX or XLS) or a CSV file.")

def main():
    st.title("Microsoft Project")

    uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx", "xls", "csv"])

    if uploaded_file is not None:
        file_extension = uploaded_file.name.split('.')[-1].lower()

        if file_extension in ('xlsx', 'xls'):
            st.text("Excel file uploaded.")
            process_files(uploaded_file)
        elif file_extension == 'csv':
            st.text("CSV file uploaded.")
            process_files(uploaded_file)

    # Check if the Material Classification page should be shown
    if st.experimental_get_query_params().get("material_classification"):
        material_classification_page()

if __name__ == "__main__":
    main()
