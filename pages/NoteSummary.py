
import streamlit as st
import openai
from AI_Summary import generate_summary_and_questions

openai.api_key = st.secrets["API_KEY"]
st.title("Notes Summary and Study Question Generator")
user_notes = st.text_area("Enter your educational notes:")
generate_summary = st.checkbox(f"Generate 5 Study Questions")
generate_links = st.checkbox(f"Suggest Helpful Resources")

with st.spinner("Loading..."):
    if st.button("Generate"):
        if user_notes:
            generated_text = generate_summary_and_questions(user_notes, generate_summary, generate_links)
            st.subheader("Output:")
            st.write(generated_text)
            st.success("Done!")
        else:
            st.warning("Please enter your notes before generating the output.")