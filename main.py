import streamlit as st
import os
import openai
from NoteMaker import generate_summary_and_questions
from StudyPlan import generate_studyplan

openai.api_key = st.secrets["API_KEY"]
st.title("Notes Summary and Study Question Generator")
user_notes = st.text_area("Enter your educational notes:")
generate_summary = st.checkbox(f"Generate 5 Study Questions")
generate_links = st.checkbox(f"Suggest Helpful Resources")

with st.spinner("Loading..."):
# Generate summary or study questions when the user submits the notes
    if st.button("Generate"):
        if user_notes:
            generated_text = generate_summary_and_questions(user_notes, generate_summary, generate_links)
            st.subheader("Output:")
            st.write(generated_text)
            st.success("Done!")
        else:
            st.warning("Please enter your notes before generating the output.")

    if st.button("Generate"):
        if user_notes2:
            generated_text2 = generate_studyplan(user_notes2)
            st.subheader("Output:")
            st.write(generated_text2)
            st.success("Done!")
        else:
            st.warning("Please enter your notes before generating the output.")


