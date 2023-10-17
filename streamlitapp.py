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
            show_material_classification(df)

def flag_duplicates(df):
    # Your duplicate flagging logic here
    pass

def process(uploaded_file):
    try:
        if uploaded_file:
            st.text("Your file is being processed...")
            # Replace this with your actual classification logic
            time.sleep(5)
            st.text("Processing complete")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

def show_material_classification(df):
    if st.button("Back to File Upload"):
        st.session_state.show_material_classification = False  # Hide Material Classification section
    else:
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

    if "show_material_classification" not in st.session_state:
        st.session_state.show_material_classification = False  # Initialize the flag

    if not st.session_state.show_material_classification:
        uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx", "xls", "csv"])
        if uploaded_file is not None:
            file_extension = uploaded_file.name.split('.')[-1].lower()

            if file_extension in ('xlsx', 'xls'):
                st.text("Excel file uploaded.")
                process_files(uploaded_file)
            elif file_extension == 'csv':
                st.text("CSV file uploaded.")
                process_files(uploaded_file)

    if st.session_state.show_material_classification:
        show_material_classification(None)

if __name__ == "__main__":
    main()
