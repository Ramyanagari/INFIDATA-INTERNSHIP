import streamlit as st


acname=st.text_input("enter customer name")
cid=st.number_input("enter customer id")
units=st.number_input("enter no_of_units")

if(units<=100):
    charge=units*0
    st.write("electricity charge is:",charge)
elif(units>=100 and units<=200):
    charge = (units-100) *5
    st.write("electricity charge is:", charge)
elif (units >= 200):
    charge = (units - 100) * 10
    st.write("electricity charge is:", charge)