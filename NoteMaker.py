import streamlit as st
import openai
from AI_Summarizer import generate_summary_and_questions
from st_pages import Page, show_pages, add_page_title

st.set_page_config(page_title = "This is a Multipage WebApp", page_icon="📓") 
st.title("This is the Home Page Geeks.") 
st.sidebar.success("Select Any Page from here1") 

show_pages(
    [
        Page("NoteMaker.py", "Home", "🏠"),
        Page("pages/Chatbot.py", "Study Pal", ":books:"),
        Page("pages/Note_Maker.py", "Note Maker", ":books:"),
        Page("pages/StudyPlan.py", "Study Plan", ":books:"),
    ]
)







