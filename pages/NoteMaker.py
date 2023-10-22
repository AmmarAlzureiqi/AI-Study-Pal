import streamlit as st
import openai

def generate_studyplan(notes):
    prompt = f"Can you make me a study plan for these I have 2 weeks: {notes}"

    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "YOU ARE A NOTE SUMMARIZING ASSISTANT"},
        {"role": "user", "content": prompt}
    ]
    )

    generated_text = response['choices'][0]['message']['content'] #response.choices[0].text.strip()
    return generated_text


openai.api_key = st.secrets["API_KEY"]
st.title("Notes Summary and Study Question Generator")
user_notes = st.text_area("Enter your educational notes:")
generate_summary = st.checkbox(f"Generate 5 Study Questions")
generate_links = st.checkbox(f"Suggest Helpful Resources")


with st.spinner("Loading..."):
    if st.button("Generate"):
        if user_notes:
            generated_text = generate_studyplan(user_notes)
            st.subheader("Output:")
            st.write(generated_text)
            st.success("Done!")
        else:
            st.warning("Please enter your notes before generating the output.")



