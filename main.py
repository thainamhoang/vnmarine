import streamlit as st 
import pandas as pd 

DOCUMENT_ID = "1GaNK6xiOjMafcZ5DdEy_Hato-sol-BCukgJyiejT6Lo"
TAB_NAME = "Sheet1"
URL = f"https://docs.google.com/spreadsheets/d/{DOCUMENT_ID}/gviz/tq?tqx=out:csv&sheet={TAB_NAME}"


st.set_page_config(page_title="Tồn kho", layout="wide", initial_sidebar_state="expanded")

st.title("Hàng tồn kho")

# Load df
df = pd.read_csv(URL)
df.dropna(subset=["Mã hàng"], inplace=True)

# Sidebar 
search_query = st.sidebar.text_input("Nhập mã hàng hoá")

unique_dropdown = df["Kho"].unique()
selected_value = st.sidebar.selectbox("Chọn Kho", options=unique_dropdown)

search_button = st.sidebar.button("Tìm kiếm")

if search_button:
    filtered = df[df["Mã hàng"].str.contains(search_query, case=False)]
    filtered = filtered[filtered["Kho"] == selected_value]
else:
    filtered = df
st.dataframe(filtered, use_container_width=True)

if len(filtered) == 1:
    with st.container():
        data = filtered.iloc[0]
        for col, row in data.items():
            if col == "Link" and isinstance(row, str):
                print(f"xxx: {row}, {type(row)}")
                st.image(row, caption="Image")
            else:
                st.write(f"{col}: {row}")
