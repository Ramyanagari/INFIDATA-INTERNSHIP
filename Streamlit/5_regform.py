import streamlit as st
import datetime
st.title('Registration Form')

my_form=st.form(key='form-1')

fname=my_form.text_input('First Name:')
lname=my_form.text_input('last Name:')
email=my_form.text_input('Email')
mobile=my_form.text_input('mobile num:')

gender=my_form.radio('Gender',('Male','Female'))

age=my_form.slider('Age:',1,70)
DateOfBirthday=my_form.date_input('Enter Birthdate:',min_value=datetime.date(1980,1,1))

address=my_form.text_area('Enter Address:')

file=my_form.file_uploader("upload ur resume:")


submit=my_form.form_submit_button('submit')


st.write('Name is'+fname+' ',lname)
st.write('Email is ',email)
st.write('Gender is ',gender)
st.write('Age is ',age)
st.write('Birthday is',bday)
st.write('Address is',address)
st.success(file)