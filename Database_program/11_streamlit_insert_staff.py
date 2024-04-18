import streamlit as st


st.info("student registartion")

emp_id=st.number_input("emo_id:")
f_name=st.text_input('f_name')
l_name=st.text_input('l_name')
j_grade=st.text_input('j_garde')
dept_id=st.number_input('dept_id')
salary=st.number_input('salary')
j_id=st.text_input('j_id')
dept_name=st.text_input('dept_name')
mobile=st.text_input('mobile')
email=st.text_input('email')

def sub():
    import mysql.connector
    #create the connection object
    myconn=mysql.connector.connect(host='localhost',user='root',password="",database="company")
    #creating the cursor object
    cur=myconn.cursor()


    sql="insert into staff(emp_id,f_name,l_name,j_grade,dept_id,dept_name,mobile,email)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val=(emp_id,f_name,l_name,j_grade,dept_id,salary,j_id,dept_name,mobile,email)


    try:

        #insert the values into the table
        cur.execute(sql, val)
        myconn.cpmmit()  #commit the transaction
        print("data inserted")


    except Exception as e:
        print("can not process:",e)
        myconn.rollback()

    print(cur.rowcount, "record inserted1")
    st.success("Registration Success")
    myconn.close()

def set_state(i):
    st.session_state.stage = i
    st.write("i value is:",i)

if 'stage' not in st.session_state:
    st.session_state.stage = 0

if st.session_state.stage == 0:
    st.button('INSERT', on_click=set_state, args=[1])


if st.session_state.stage >= 1:
    sub()
