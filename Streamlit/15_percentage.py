import streamlit as st
n=st.number_input("enter the value of student")
if(n>90):
    st.write("gradeA")
elif(n>80 and n<90):
    st.write("gradeB")
elif(n>60 and n<=80):
    st.write("gradec")
else:
    st.write("gradeD")
    st.success(n)