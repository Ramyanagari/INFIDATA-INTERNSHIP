import streamlit as st

st.sidebar.title("Reg Form")
with st.form(key='From1'):
    with st.sidebar:


        user_word = st.text_input("Enter a keyword")
        select_language = st.radio('Tweet language',('All','English','hindi'))
        include_retweets = st.checkbox('Include retweets in data')
        num_of_tweets = st.number_input('Minimum number of tweets',190)
        submitted = st.form_submit_button(label='Search Twitter')
st.write("keyword is:",user_word)
st.title("language is:",select_language)