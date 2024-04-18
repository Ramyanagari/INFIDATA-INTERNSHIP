import streamlit as st

st.bar_chart({"data":[1,5,2,6,2,1]})

with st.expander("see explanation"):
    st.write("The chart above shows some numbers i picked for you:")
    st.image("butterfly.png")