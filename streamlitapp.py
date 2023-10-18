import streamlit as st
import pandas as pd
import time
import base64

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/png;base64,{encoded_string});
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def center_buttons():
    st.markdown(
        """
        <style>
        .stButton {
            display: flex;
            justify-content: center;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

def process_files(df):
    st.subheader("Sorted Data:")
    st.dataframe(df, height=300)
    if df is not None:
        if st.button("Download Duplicate flagged"):
            deduplicated = flag_duplicates(df)
            st.download_button("Download Duplicated flagged", deduplicated.to_csv(), key='download_duplicates', mime='text/csv')

        if st.button("Go To Material Classification"):
            st.experimental_set_query_params(material_classification=True)  # Switch to Material Classification page

   

def flag_duplicates(df):
    # Your duplicate flagging logic here
    pass

def material_classification_page():
    pass

def add_logo(size=250):
    st.markdown(
        f"""
        <style>
        .stImage {{
            position: absolute;
            top: 0;
            left: 0;
            width: {size}px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
    st.image("eren.png", width=size)

def main():
    add_logo(size=250)
    st.title("Microsoft Project")
    add_bg_from_local("eren.png")

    st.markdown(
        """
        <style>
        .stImage {
            position: absolute;
            top: 0;
            left: 0;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx", "xls", "csv"])

    if uploaded_file is not None:
        file_extension = uploaded_file.name.split('.')[-1].lower()

        if file_extension in ('xlsx', 'xls'):
            st.text("Excel file uploaded.")
            center_buttons()
            df = pd.read_excel(uploaded_file)
            
            # Sort the DataFrame in ascending order by the first column
            df = df.sort_values(by=df.columns[0])
            
            if not df.empty:  # Check if the DataFrame is not empty
                process_files(df)  # Pass the sorted DataFrame to the function
            else:
                st.text("DataFrame is empty.")
        elif file_extension == 'csv':
            st.text("CSV file uploaded.")
            center_buttons()
            df = pd.read_csv(uploaded_file)
            
            # Sort the DataFrame in ascending order by the first column
            df = df.sort_values(by=df.columns[0])

            if not df.empty:  # Check if the DataFrame is not empty
                process_files(df)  # Pass the sorted DataFrame to the function
            else:
                st.text("DataFrame is empty.")

if __name__ == "__main__":
    main()
