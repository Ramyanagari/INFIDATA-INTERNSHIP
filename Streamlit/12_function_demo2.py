import streamlit as st
def add():
    n1=st.number_input("enter n1 int value:")
    n2=st.number_input("enter n2 int value:")
    sum=n1+n2
    st.write("add of 2 int num iks:")
    st.success(sum)

def sub():
    n1=st.number_input("enter n1 int value:")
    n2=st.number_input("enter n2 int value:")
    res=n1-n2
    st.write("sub of 2 int num is:")
    st.success(res)

def set_state(i):
    st.session_state.stage = i
    st.write("i value is:",i)

st.header("Addition program")
st.info("click a button to proceed:")

if 'stage' not in st.session_state:
    st.session_state.stage = 0

if st.session_state.stage == 0:
    st.button('ADD', on_click=set_state,args=[1])

if st.session_state.stage == 0:
    st.button('SUB', on_click=set_state, args=[2])

if st.session_state.stage == 1:
    add()

if st.session_state.stage == 2:
    sub()