import streamlit as st
import pandas as pd

# Define a function to perform keyword matching
def keyword_matching(data):
    # Add your keyword matching logic here
    # This is just a placeholder example
    matched_data = data[data.str.contains("keyword", case=False)]
    return matched_data

def process_files(uploaded_file):
    if uploaded_file:
        df = pd.read_excel(uploaded_file, nrows=30)
        first_column = df.iloc[:, 0]

        st.dataframe(first_column, height=300)  # Display only the first column with a fixed height

        col1, col2 = st.columns(2)

        if col1.button("Remove Duplicates"):
            # Check for duplicates in the first column by default and remove them
            first_column_no_duplicates = first_column.drop_duplicates()
            col1.dataframe(first_column_no_duplicates, height=300)  # Display the first column without duplicate values

        if col2.button("Submit anyway"):
            # Call the keyword matching function when "Submit anyway" is clicked
            matched_data = keyword_matching(first_column)
            col2.dataframe(matched_data, height=300)  # Display the matched data

def main():
    st.title("First Project")

    uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx", "xls"])

    if uploaded_file is not None:
        file_extension = uploaded_file.name.split('.')[-1]

        if file_extension in ('xlsx', 'xls'):
            st.text("Excel file uploaded. You can process it here.")
            process_files(uploaded_file)

        else:
            st.text("Unsupported file type. Please upload an Excel file (XLSX or XLS).")

if __name__ == "__main__":
    main()
