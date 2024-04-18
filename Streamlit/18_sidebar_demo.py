import streamlit as st

#using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted",
    ("Email","Home phone","Mobile phone")
)

#using "with" notation
with st.sidebar:
    add_radio=st.radio(
        "choose a shipping method",
        ("Standard (5-15days)","Express (2-5 days)")
    )
    name=st.text("Enter Customer Name:")
