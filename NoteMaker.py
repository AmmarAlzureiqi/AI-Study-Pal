import streamlit as st
import os
import openai


#openai.api_key = st.text_area("Enter API Key")
openai.api_key = st.secrets["API_KEY"]

def generate_summary_and_questions(notes, generate_questions=True):
    prompt = f"Summarize the following notes: {notes}"
    if not generate_questions:
        prompt = f"CAN YOU GIVE ME A SUMMARY OF THESE NOTES {notes} THAT IS 33% THE LENGTH OF THE ORIGINAL NOTES"
    else:
        prompt = f"CAN YOU GIVE ME A SUMMARY OF THESE NOTES {notes} THAT IS 33% THE LENGTH OF THE ORIGINAL NOTES, AND CREATE 3-5 STUDY QUESTIONS"
    
    #response = openai.Completion.create(
        #engine="text-davinci-003",
        #prompt=prompt,
        #max_tokens=250,  # Adjust the max_tokens based on your requirements
        #n=1,
    #)
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "YOU ARE A NOTE SUMMARIZING ASSISTANT"},
        {"role": "user", "content": prompt}
    ]
    )

    generated_text = response['choices'][0]['message']['content'] #response.choices[0].text.strip()
    return generated_text

# Streamlit app
st.title("Educational Notes Summarizer and Study Question Generator")

# Text input for user's notes
user_notes = st.text_area("Enter your educational notes:")

# Checkbox to choose between summary and study questions
generate_summary = st.checkbox(f"Generate Summary (check to generate 5 study questions)")


# Generate summary or study questions when the user submits the notes
if st.button("Generate"):
    if user_notes:
        generated_text = generate_summary_and_questions(user_notes, generate_summary)
        st.subheader("Output:")
        st.write(generated_text)
    else:
        st.warning("Please enter your notes before generating the output.")


