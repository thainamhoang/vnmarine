import streamlit as st
import pandas as pd

DOCUMENT_ID = "1GaNK6xiOjMafcZ5DdEy_Hato-sol-BCukgJyiejT6Lo"
TAB_NAME = "Sheet2"
URL = f"https://docs.google.com/spreadsheets/d/{DOCUMENT_ID}/gviz/tq?tqx=out:csv&sheet={TAB_NAME}"


st.set_page_config(
    page_title="Tồn kho", layout="wide", initial_sidebar_state="expanded"
)

st.title("Hàng tồn kho")

# Load df
df = pd.read_csv(URL)
df.dropna(subset=["Mã hàng"], inplace=True)

# Sidebar
search_query = st.sidebar.text_input("Nhập mã hàng hoá")

# Kho
# Remove nan kho
kho_dd_val = df["Kho"].unique()
kho_selected_val = st.sidebar.selectbox("Chọn Kho", options=kho_dd_val)

# Category
cat_dd_val = df["Category"].unique()
cat_selected_val = st.sidebar.selectbox("Chọn Loại", options=cat_dd_val)

# Brand
brand_dd_val = df["Brand"].unique()
brand_selected_val = st.sidebar.selectbox("Chọn Nhãn hiệu", options=brand_dd_val)


search_button = st.sidebar.button("Tìm kiếm")

if search_button:
    filtered = df[df["Mã hàng"].str.contains(search_query, case=False)]
    if cat_selected_val:
        filtered = filtered[filtered["Category"] == cat_selected_val]
    if brand_selected_val:
        filtered = filtered[filtered["Brand"] == brand_selected_val]
    if kho_selected_val:
        filtered = filtered[filtered["Kho"] == kho_selected_val]

else:
    filtered = df
st.dataframe(filtered.iloc[:, :8].reset_index(drop=True), use_container_width=True)

if len(filtered) == 1:
    with st.container():
        data = filtered.iloc[0]
        for col, row in data.items():
            if col == "Link" and isinstance(row, str):
                print(f"xxx: {row}, {type(row)}")
                split = row.split(",")
                for s in split:
                    st.image(s, caption="")
            else:
                st.write(f"{col}: {row}")
