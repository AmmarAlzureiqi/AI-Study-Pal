import streamlit as st
import os
import openai
from NoteMaker import generate_summary_and_questions
from st_pages import Page, show_pages, add_page_title

add_page_title() # By default this also adds indentation

# Specify what pages should be shown in the sidebar, and what their titles and icons
# should be
show_pages(
    [
        Page("streamlit_app.py", "Home", "🏠"),
        Page("other_pages/page2.py", "Page 2", ":books:"),
        Section("My section", icon="🎈️"),
        # Pages after a section will be indented
        Page("Another page", icon="💪"),
        # Unless you explicitly say in_section=False
        Page("Not in a section", in_section=False)
    ]
)


openai.api_key = st.secrets["API_KEY"]
st.title("Notes Summary and Study Question Generator")
user_notes = st.text_area("Enter your educational notes:")
generate_summary = st.checkbox(f"Generate 5 Study Questions")

with st.spinner("Loading..."):
# Generate summary or study questions when the user submits the notes
    if st.button("Generate"):
        if user_notes:
            generated_text = generate_summary_and_questions(user_notes, generate_summary)
            st.subheader("Output:")
            st.write(generated_text)
            st.success("Done!")
        else:
            st.warning("Please enter your notes before generating the output.")


with st.sidebar:
    st.header("Header")
    st.subheader("subhead")


