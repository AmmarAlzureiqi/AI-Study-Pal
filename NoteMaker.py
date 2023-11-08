import streamlit as st
from st_pages import Page, show_pages

st.set_page_config(page_title = "AI Study Pal", page_icon="📓") 
st.title("All in One AI Study Assistant!") 
st.sidebar.success("Select Any Page from here") 

st.subheader("Welcome to the All in one AI Study Assistant!")
st.text("Welcome to our AI-powered student support hub! Here, we've harnessed the power of artificial intelligence to assist you in your educational journey. Whether you need a study partner or quick note summaries, our AI study chatbot is here to help. Additionally, our note summarizer page provides concise, easy-to-understand summaries of your study materials, while our study plan generator can tailor a study plan just for you. Empower your learning experience with our suite of AI tools, designed to make your student life more efficient and effective.")

st.subheader("Available tools to assist with your studies!")
st.text('- Study Pal')
st.text('- Note Maker')
st.text('- Study Plan Generator')

show_pages(
    [
        Page("NoteMaker.py", "Home", "🏠"),
        Page("pages/Chatbot.py", "Study Pal", "🤖"),
        Page("pages/Note_Maker.py", "Note Maker", ":books:"),
        Page("pages/StudyPlan.py", "Study Plan", ":books:"),
    ]
)







