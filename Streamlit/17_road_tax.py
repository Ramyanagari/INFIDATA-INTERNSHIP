import streamlit as st
bike_price=st.number_input("bike_price")
st.write("the road tax you should pay is")
if bike_price>100000:
    val=bike_price*0.15
    st.write("the road tax is:",val)
elif bike_price>50000 and bike_price<=100000:
    val2=bike_price*0.1
    st.write("the road tax is:".val2)
elif bike_price > 50000 and bike_price <= 0:
    val2 = bike_price * 0.05
    st.write("the road tax is:".val3)
else:

    st.write("unknown")
    st.success(bike_price)