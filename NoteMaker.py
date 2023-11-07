import streamlit as st
import openai
from AI_Summarizer import generate_summary_and_questions
from st_pages import Page, show_pages, add_page_title

st.set_page_config(page_title = "AI Study Pal", page_icon="📓") 
st.title("All in One AI Study Assistant!") 
st.sidebar.success("Select Any Page from here") 

show_pages(
    [
        Page("NoteMaker.py", "Home", "🏠"),
        Page("pages/Chatbot.py", "Study Pal", "🤖"),
        Page("pages/Note_Maker.py", "Note Maker", ":books:"),
        Page("pages/StudyPlan.py", "Study Plan", ":books:"),
    ]
)







