import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.title("Stroke Prediction Dashboard")
st.markdown("The dashboard will help a research to get to know\
more about the given datasets and it's output")

#sidebar
st.sidebar.title("Select Visual Charts")
st.sidebar.markdown("Select the Charts/plots accordingly:")

data=pd.read_csv("demo_data_set.csv")

chart_visual=st.sidebar.selectbox('select chart/plot type',('Linechart','Bar chart','Bubble chart'))

st.sidebar.checkbox("Show Analysis by Smoking status",True,key=1)
selected_status=st.sidebar.selectbox('Select Smoking Status',
                                     options=['Formerly_Smoked','Smoked','Never_Smoked','Unknown'])

fig=go.Figure()
if chart_visual=='Linechart':
    if selected_status=='Formerly_Smoked':
        fig.add_trace(go.Scatter(x=data.Country,y=data.formerly_smoked,
                                 mode='lines',
                                 name='Formerly_Smoked'))
    elif selected_status=='Smoked':
        fig.add_trace(go.Scatter(x=data.Country,y=data.Smokes,
                                 mode='lines',
                                 name='Smoked'))
    elif selected_status == 'Never_Smoked':
        fig.add_trace(go.Scatter(x=data.Country, y=data.Never_Smoked,
                                 mode='lines',
                                 name='Never_Smoked'))
    elif selected_status == 'Unknown':
        fig.add_trace(go.Scatter(x=data.Country, y=data.Unknown,
                                  mode='lines',
                                  name='Unknown'))
elif chart_visual=='Bar chart':
    if selected_status=='Formerly_Smoked':
        fig.add_trace(go.Bar(x=data.Country,y=data.formerly_smoked,
                                 name='Formerly_Smoked'))
    elif selected_status=='Smoked':
        fig.add_trace(go.Bar(x=data.Country,y=data.Smokes,
                                 name='Smoked'))
    elif selected_status == 'Never_Smoked':
        fig.add_trace(go.Bar(x=data.Country,y=data.Smokes,
                                 name='Never_Smoked'))
    elif selected_status == 'Unknown':
        fig.add_trace(go.Bar(x=data.Country, y=data.Smokes,
                             name='Unknown'))
if chart_visual=='Bubble Chart':
    if selected_status=='Formerly_Smoked':
        fig.add_trace(go.Scatter(x=data.Country,y=data.formerly_smoked,
                                 mode='markers',
                                 marker_size=[20,60,80,50,40,70],
                                 name='Formerly_Smoked'))
    elif selected_status=='Smoked':
        fig.add_trace(go.Scatter(x=data.Country, y=data.Smokes,
                                 mode='markers',
                                 marker_size=[10, 40, 60, 90, 20, 50],
                                 name='Smoked'))
    elif selected_status == 'Never_Smoked':
         fig.add_trace(go.Scatter(x=data.Country, y=data.Never_Smoked,
                             mode='markers',
                             marker_size=[30, 40, 60, 50, 20, 10],
                             name='Never_Smoked'))
    elif selected_status == 'Unknown':
         fig.add_trace(go.Scatter(x=data.Country, y=data.Unknown,
                             mode='markers',
                             marker_size=[10, 20, 30, 40, 50, 60],
                             name='Unknown'))

st.plotly_chart(fig,use_container_width=True)



