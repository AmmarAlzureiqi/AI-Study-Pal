import streamlit as st
import openai
import NoteMaker


openai.api_key = st.secrets["API_KEY"]
st.title("Educational Notes Summarizer and Study Question Generator")
user_notes = st.text_area("Enter your educational notes:")
generate_summary = st.checkbox(f"Generate Summary (check to generate 5 study questions)")

# Generate summary or study questions when the user submits the notes
if st.button("Generate"):
    if user_notes:
        generated_text = NoteMaker.generate_summary_and_questions(user_notes, generate_summary)
        st.subheader("Output:")
        st.write(generated_text)
    else:
        st.warning("Please enter your notes before generating the output.")
