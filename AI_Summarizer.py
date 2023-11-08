import streamlit as st
import openai

openai.api_key = st.secrets["API_KEY"]

def generate_summary_and_questions(notes, generate_questions=True, generate_links=False):
    prompt = f"Summarize the following notes: {notes}"
    if generate_questions and generate_links:
        prompt = f"CAN YOU GIVE ME A SUMMARY OF THESE NOTES {notes} THAT IS 33% THE LENGTH OF THE ORIGINAL NOTES, AND CREATE 3-5 STUDY QUESTIONS and include helpful 2 helpful websites"
    elif generate_questions:
        prompt = f"CAN YOU GIVE ME A SUMMARY OF THESE NOTES {notes} THAT IS 33% THE LENGTH OF THE ORIGINAL NOTES, AND CREATE 3-5 STUDY QUESTIONS"
    elif generate_links:
        prompt = f"CAN YOU GIVE ME A SUMMARY OF THESE NOTES {notes} THAT IS 33% THE LENGTH OF THE ORIGINAL NOTES and include helpful 2 helpful websites"
    else:
        prompt = f"CAN YOU GIVE ME A SUMMARY OF THESE NOTES {notes} THAT IS 33% THE LENGTH OF THE ORIGINAL NOTES"

        
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "YOU ARE A NOTE SUMMARIZING ASSISTANT"},
        {"role": "user", "content": prompt}
    ]
    )

    generated_text = response['choices'][0]['message']['content'] #response.choices[0].text.strip()
    return generated_text




