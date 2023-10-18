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

def compare_columns(df):
    # Step 1: Compare (column 1) with (column 3)
    compare_noun = df.iloc[:, 1].str.strip() == df.iloc[:, 3].str.strip()

    # Step 2: Compare (column 2) with (column 4)
    compare_modifier = df.iloc[:, 2].str.strip() == df.iloc[:, 4].str.strip()

    matching_noun_rows = compare_noun
    matching_modifier_rows = compare_modifier

    
    accuracy_noun = matching_noun_rows.sum() / len(df)
    accuracy_modifier = matching_modifier_rows.sum() / len(df)

 
    st.write(f"Accuracy for Nouns: {accuracy_noun:.2%}")


    st.write(f"Accuracy for Modifiers: {accuracy_modifier:.2%}")


def process_files(df):
    if df is not None:
        compare_columns(df)


        if st.button("Download Duplicate flagged"):
            deduplicated = flag_duplicates(df)
            st.download_button("Download Duplicated flagged", deduplicated.to_csv(), key='download_duplicates', mime='text/csv')

        if st.button("Go To Material Classification"):
            st.experimental_set_query_params(material_classification=True)  # Switch to Material Classification page

        st.subheader("Uploaded Data:")
        st.dataframe(df, height=300)

       

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

    uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx", "xls"])

    if uploaded_file is not None:
        file_extension = uploaded_file.name.split('.')[-1]

        if file_extension in ('xlsx', 'xls'):
            st.text("Excel file uploaded. You can process it here.")
            df = pd.read_excel(uploaded_file)
            process_files(df)  # Display and process the uploaded data
        else:
            st.text("Unsupported file type. Please upload an Excel file (XLSX or XLS).")

if __name__ == "__main__":
    main()
