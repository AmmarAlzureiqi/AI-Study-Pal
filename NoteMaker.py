import streamlit as st
from st_pages import Page, show_pages

st.set_page_config(page_title = "AI Study Pal", page_icon="📓") 
st.title("All in One AI Study Assistant!") 
st.sidebar.success("Select Any Page from here") 

st.subheader("Welcome to the All in one AI Study Assistant!")
st.text('hello')

show_pages(
    [
        Page("NoteMaker.py", "Home", "🏠"),
        Page("pages/Chatbot.py", "Study Pal", "🤖"),
        Page("pages/Note_Maker.py", "Note Maker", ":books:"),
        Page("pages/StudyPlan.py", "Study Plan", ":books:"),
    ]
)







