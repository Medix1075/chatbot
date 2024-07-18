import streamlit as st
import Input
import Mood
from Mood import chain
import uuid
import time

custom_css = """
<style>
    .title {
        font-size: 70px;
        font-family: 'Courier New', Courier, monospace;
    }
    
    .headline {
        font-size: 40px;
        font-family: 'Courier New', Courier, monospace;
    }
    .text-input {
        font-size: 20px;
    }
</style>
"""

# Embed the custom CSS in the Streamlit app
st.markdown(custom_css, unsafe_allow_html=True)

# Set the title of the app with custom CSS class

st.markdown('<p class="title">Customer Care</p>', unsafe_allow_html=True)

st.markdown('<p class="headline">Helpdesk</p>', unsafe_allow_html=True)
service = st.sidebar.selectbox("Select Service",("Automated Response Generation", "Personalized Customer Engagement"))

if service == "Automated Response Generation":

    st.markdown('<p class="text-input">Ask me a Question or a Query!</p>', unsafe_allow_html=True)
    query = st.text_input('Type below...')
    info = Input.question(query)
    st.write(info)

if service == "Personalized Customer Engagement":

    option = st.sidebar.selectbox("Select", ("ChatBot","Mood_Music"))
    if option == "ChatBot":
        if 'queries' not in st.session_state:
            st.session_state.queries = []
        if 'responses' not in st.session_state:
            st.session_state.responses = []

        st.markdown('<p class="text-input">Ask me a Question or a Query!</p>', unsafe_allow_html=True)
        for i, query in enumerate(st.session_state.queries):
            st.text_input(f"Previous Query {i + 1}", value=query, key=f'query_{i}', disabled=True)
            st.write(st.session_state.responses[i])

        query = st.text_input('Type your question below...', key='new_query')
        if st.button('Submit', key='submit_button'):
            response = Input.question(query)
            st.session_state.queries.append(query)
            st.session_state.responses.append(response)
            st.experimental_rerun()

    if option == "Mood_Music":
        st.markdown('<p class="text-input">How is your mood today?</p>', unsafe_allow_html=True)
        quest = st.text_input('Type below...')
        if quest:
            info = chain(quest)
            st.write(info["result"])






    

