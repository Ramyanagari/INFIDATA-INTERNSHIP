import streamlit as st
import datetime
st.title('Student Registration Form')
my_form=st.form(key='form')

fname=my_form.text_input('First Name:')
lname=my_form.text_input('Last Name:')
email=my_form.text_input('Email:')
mobile=my_form.text_input('Mobile.no:')

gender=my_form.radio('Gender',('Male','Female'))

bday=my_form.date_input('Enter Birthdate:',min_value=datetime.date(1980,1,1))

address=my_form.text_area('Enter Address:')

city=my_form.text_input('Enter the city:')
pin=my_form.text_input('Enter the pin:')
state=my_form.text_input('Enter the state:')
qualification=my_form.selectbox('Qualification', [None,'B.sc','B.tech','M.sc','B.com','BZC'])
specialization=my_form.radio('Specialization',('Computer science','Information technology','Computer architecture','Tele communication'))
password=my_form.text_input('Password:')
submit=my_form.form_submit_button('Register')