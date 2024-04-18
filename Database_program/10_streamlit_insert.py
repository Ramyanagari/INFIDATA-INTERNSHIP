import streamlit as st

st.info("student registration")

name=st.text_input('name')
id=st.number_input('id')
branch=st.text_input('branch')
email=st.text_input('email')
mobile=st.text_input('mobile')


def add():
    import mysql.connector
    #create the connection object
    myconn=mysql.connector.connect(host="localhost",user="root",password="",database="college")
    #creating the cursor object
    cur=myconn.cursor()

    sql="insert into student1(name,id,branch,email,mobile)values(%s,%s,%s,%s,%s)"
    val=(name,id,branch,email,mobile)

    try:
        # inserting the values into the table
        cur.execute(sql, val)
        myconn.commit() # commit the transcation
        print("data inserted")


    except Exception as e:
        print("can not process:",e)
        myconn.close()

    print(cur.rowcount, "record inserted!")
    st.success("Registration success")
    myconn.close()

def set_state(i):
    st.session_state.stage = i
    st.write("i value is:",i)

if 'stage' not in st.session_state:
    st.session_state.stage = 0

if st.session_state.stage == 0:
    st.button('INSERT', on_click=set_state, args=[1])

if st.session_state.stage >=1:
    add()